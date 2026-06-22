"""Batched .docx generation for a matter folder.

When lite mode is on, drafts are saved as .md only at generation time. Run
`ailawfirm-india finalize <matter>` at end of session to batch-convert every
.md to .docx via nice'd pandoc — same content, same fidelity, one process
burst instead of per-keystroke heat.
"""

import shutil
import subprocess
from pathlib import Path


def finalize_matter(matter_dir: str, max_cpu: int = 80) -> int:
    """Walk a matter folder, generate .docx for every .md that's newer than
    its paired .docx (or has no .docx yet).

    Args:
        matter_dir: path to the matter folder
        max_cpu: informational soft cap (used to inform user; pandoc itself
                 doesn't honour a CPU cap, but we use `nice` to deprioritise)

    Returns:
        Exit code: 0 on full success, N = number of failed conversions.
    """
    root = Path(matter_dir).expanduser().resolve()
    if not root.is_dir():
        print(f"\n  ❌ Not a directory: {root}")
        return 1

    if not shutil.which("pandoc"):
        print("\n  ❌ pandoc not installed.")
        print("     macOS:   brew install pandoc")
        print("     Linux:   sudo apt-get install -y pandoc")
        return 2

    mds = sorted(p for p in root.rglob("*.md") if not p.name.startswith("."))
    if not mds:
        print(f"\n  No .md files found under {root}")
        return 0

    print(f"\n  Finalizing {len(mds)} drafts → .docx (nice'd · target max_cpu={max_cpu}%)\n")

    failed = 0
    converted = 0
    for md in mds:
        docx = md.with_suffix(".docx")
        rel = md.relative_to(root)
        if docx.exists() and docx.stat().st_mtime >= md.stat().st_mtime:
            print(f"  SKIP (up-to-date): {rel}")
            continue
        try:
            rc = subprocess.call(
                [
                    "nice",
                    "-n",
                    "10",
                    "pandoc",
                    str(md),
                    "-o",
                    str(docx),
                    "--from=markdown+pipe_tables+yaml_metadata_block",
                ]
            )
            if rc == 0:
                converted += 1
                print(f"  ✓ {rel} → .docx")
            else:
                failed += 1
                print(f"  ✗ {rel} (pandoc rc={rc})")
        except Exception as e:
            failed += 1
            print(f"  ✗ {rel} ({e})")

    print(
        f"\n  Done. {converted} converted · {failed} failed · {len(mds) - converted - failed} up-to-date."
    )
    return failed
