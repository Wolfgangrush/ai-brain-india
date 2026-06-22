#!/usr/bin/env python3
"""
Brain — Give your AI a memory. No API key required.

Two ways to ingest:
  Projects:      brain mine ~/projects/my_app          (code, docs, notes)
  Conversations: brain mine ~/chats/ --mode convos     (Claude, ChatGPT, Slack)

Same palace. Same search. Different ingest strategies.

Commands:
    brain init <dir>                  Detect rooms from folder structure
    brain split <dir>                 Split concatenated mega-files into per-session files
    brain mine <dir>                  Mine project files (default)
    brain mine <dir> --mode convos    Mine conversation exports
    brain search "query"              Find anything, exact words
    brain wake-up                     Show L0 + L1 wake-up context
    brain wake-up --wing my_app       Wake-up for a specific project
    brain status                      Show what's been filed

Examples:
    brain init ~/projects/my_app
    brain mine ~/projects/my_app
    brain mine ~/chats/claude-sessions --mode convos
    brain search "why did we switch to GraphQL"
    brain search "pricing discussion" --wing my_app --room costs
"""

import os
import sys
import argparse
from pathlib import Path

from .config import BrainConfig

# Upstream repo for `ailawfirm-india update` — substituted per firm at package level.
REPO_URL = "git+https://github.com/Wolfgangrush/ai-law-firm-india.git"


def cmd_update(args):
    """Pull the latest firm code, skills, and prompts from upstream.

    Wraps `pip install --upgrade git+<REPO_URL>`. Touches firm code only —
    user matter data + the project-root CLAUDE.md are NEVER overwritten.
    """
    import subprocess

    print("\n  Updating firm code from upstream…")
    print(f"  Source: {REPO_URL}")
    print("  Your matter data + your project CLAUDE.md will NOT be touched.\n")
    cmd = [sys.executable, "-m", "pip", "install", "--upgrade", REPO_URL]
    if getattr(args, "quiet", False):
        cmd.insert(-1, "--quiet")
    rc = subprocess.call(cmd)
    if rc == 0:
        print("\n  ✅ Firm updated. Restart any open `ailawfirm-india` session.")
        print("     To see what's new in this version, run:")
        print("       ailawfirm-india status")
    else:
        print(f"\n  ❌ Update failed (exit code {rc}).")
        print("     Check your internet connection or run the command manually:")
        print(f"       pip install --upgrade {REPO_URL}")
    return rc


def cmd_lite(args):
    """Toggle lite mode (low-RAM Mac helper).

    Lite mode defers per-draft .docx generation and skips MCP-server
    autostart. Drafts are saved as .md during the session; batch-generate
    .docx via `ailawfirm-india finalize <matter>` when ready.

    Default behaviour is unchanged — lite mode is opt-in.
    """
    from .thermal import is_lite_mode, set_lite_mode

    action = getattr(args, "action", None)
    if action == "on":
        set_lite_mode(True)
        print("\n  ✓ Lite mode ON")
        print("    - per-draft .docx generation DEFERRED")
        print("    - MCP-server autostart SKIPPED")
        print("\n  When ready to file/email, batch-generate .docx:")
        print("    ailawfirm-india finalize <matter-folder>")
    elif action == "off":
        set_lite_mode(False)
        print("\n  ✓ Lite mode OFF — default behaviour restored.")
    else:
        print(f"\n  Lite mode is currently {'ON' if is_lite_mode() else 'OFF'}")
        print("  Toggle with:  ailawfirm-india lite on  |  ailawfirm-india lite off")


def cmd_doctor(args):
    """Diagnose thermal/RAM state — charger · lite mode · pandoc · memory."""
    from .thermal import run_doctor

    return run_doctor()


def cmd_finalize(args):
    """Batch-generate .docx for every .md in a matter folder."""
    from .finalize import finalize_matter

    return finalize_matter(args.matter, max_cpu=args.max_cpu)


def _copy_claude_md_template(target_dir: Path) -> None:
    """Copy templates/CLAUDE.md into the user's project root on init.

    Skipped if the user already has a CLAUDE.md (their customisations win).
    """
    import shutil

    target = Path(target_dir).expanduser().resolve() / "CLAUDE.md"
    if target.exists():
        print(f"  CLAUDE.md already present at {target} — preserving your version.")
        return
    # templates/ ships inside the package — works for both pip-installed and source checkout.
    pkg_dir = Path(__file__).resolve().parent
    candidates = [
        pkg_dir / "templates" / "CLAUDE.md",  # canonical: shipped with wheel
        pkg_dir.parent / "templates" / "CLAUDE.md",  # legacy source-checkout fallback
    ]
    for src in candidates:
        if src.exists():
            shutil.copy(src, target)
            print(f"  CLAUDE.md template written: {target}")
            print("     Edit it with your firm name + advocate details.")
            return
    print("  (templates/CLAUDE.md not found in package — skipping CLAUDE.md seed.)")


def cmd_init(args):
    import json
    from pathlib import Path
    from .entity_detector import scan_for_detection, detect_entities, confirm_entities
    from .room_detector_local import detect_rooms_local

    # Pass 1: auto-detect people and projects from file content
    print(f"\n  Scanning for entities in: {args.dir}")
    files = scan_for_detection(args.dir)
    if files:
        print(f"  Reading {len(files)} files...")
        detected = detect_entities(files)
        total = len(detected["people"]) + len(detected["projects"]) + len(detected["uncertain"])
        if total > 0:
            confirmed = confirm_entities(detected, yes=getattr(args, "yes", False))
            # Save confirmed entities to <project>/entities.json for the miner
            if confirmed["people"] or confirmed["projects"]:
                entities_path = Path(args.dir).expanduser().resolve() / "entities.json"
                with open(entities_path, "w") as f:
                    json.dump(confirmed, f, indent=2)
                print(f"  Entities saved: {entities_path}")
        else:
            print("  No entities detected — proceeding with directory-based rooms.")

    # Pass 2: detect rooms from folder structure
    detect_rooms_local(project_dir=args.dir)
    BrainConfig().init()

    # Pass 3: seed CLAUDE.md template into the user's project root (preserves existing).
    _copy_claude_md_template(Path(args.dir))


def cmd_mine(args):
    palace_path = os.path.expanduser(args.palace) if args.palace else BrainConfig().palace_path

    if args.mode == "convos":
        from .convo_miner import mine_convos

        mine_convos(
            convo_dir=args.dir,
            palace_path=palace_path,
            wing=args.wing,
            agent=args.agent,
            limit=args.limit,
            dry_run=args.dry_run,
            extract_mode=args.extract,
        )
    else:
        from .miner import mine

        mine(
            project_dir=args.dir,
            palace_path=palace_path,
            wing_override=args.wing,
            agent=args.agent,
            limit=args.limit,
            dry_run=args.dry_run,
        )


def cmd_search(args):
    from .searcher import search

    palace_path = os.path.expanduser(args.palace) if args.palace else BrainConfig().palace_path
    search(
        query=args.query,
        palace_path=palace_path,
        wing=args.wing,
        room=args.room,
        n_results=args.results,
    )


def cmd_wakeup(args):
    """Show L0 (identity) + L1 (essential story) — the wake-up context."""
    from .layers import MemoryStack

    palace_path = os.path.expanduser(args.palace) if args.palace else BrainConfig().palace_path
    stack = MemoryStack(palace_path=palace_path)

    text = stack.wake_up(wing=args.wing)
    tokens = len(text) // 4
    print(f"Wake-up text (~{tokens} tokens):")
    print("=" * 50)
    print(text)


def cmd_split(args):
    """Split concatenated transcript mega-files into per-session files."""
    from .split_mega_files import main as split_main
    import sys

    # Rebuild argv for split_mega_files argparse
    argv = [args.dir]
    if args.output_dir:
        argv += ["--output-dir", args.output_dir]
    if args.dry_run:
        argv.append("--dry-run")
    if args.min_sessions != 2:
        argv += ["--min-sessions", str(args.min_sessions)]

    old_argv = sys.argv
    sys.argv = ["brain split"] + argv
    try:
        split_main()
    finally:
        sys.argv = old_argv


def cmd_status(args):
    from .miner import status

    palace_path = os.path.expanduser(args.palace) if args.palace else BrainConfig().palace_path
    status(palace_path=palace_path)


def cmd_compress(args):
    """Compress drawers in a wing using Entity-Aliasing Dialect."""
    import chromadb
    from .dialect import Dialect

    palace_path = os.path.expanduser(args.palace) if args.palace else BrainConfig().palace_path

    # Load dialect (with optional entity config)
    config_path = args.config
    if not config_path:
        for candidate in ["entities.json", os.path.join(palace_path, "entities.json")]:
            if os.path.exists(candidate):
                config_path = candidate
                break

    if config_path and os.path.exists(config_path):
        dialect = Dialect.from_config(config_path)
        print(f"  Loaded entity config: {config_path}")
    else:
        dialect = Dialect()

    # Connect to palace
    try:
        client = chromadb.PersistentClient(path=palace_path)
        col = client.get_collection("brain_drawers")
    except Exception:
        print(f"\n  No palace found at {palace_path}")
        print("  Run: brain init <dir> then brain mine <dir>")
        sys.exit(1)

    # Query drawers in the wing
    where = {"wing": args.wing} if args.wing else None
    try:
        kwargs = {"include": ["documents", "metadatas"]}
        if where:
            kwargs["where"] = where
        results = col.get(**kwargs)
    except Exception as e:
        print(f"\n  Error reading drawers: {e}")
        sys.exit(1)

    docs = results["documents"]
    metas = results["metadatas"]
    ids = results["ids"]

    if not docs:
        wing_label = f" in wing '{args.wing}'" if args.wing else ""
        print(f"\n  No drawers found{wing_label}.")
        return

    print(
        f"\n  Compressing {len(docs)} drawers"
        + (f" in wing '{args.wing}'" if args.wing else "")
        + "..."
    )
    print()

    total_original = 0
    total_compressed = 0
    compressed_entries = []

    for doc, meta, doc_id in zip(docs, metas, ids):
        compressed = dialect.compress(doc, metadata=meta)
        stats = dialect.compression_stats(doc, compressed)

        total_original += stats["original_chars"]
        total_compressed += stats["compressed_chars"]

        compressed_entries.append((doc_id, compressed, meta, stats))

        if args.dry_run:
            wing_name = meta.get("wing", "?")
            room_name = meta.get("room", "?")
            source = Path(meta.get("source_file", "?")).name
            print(f"  [{wing_name}/{room_name}] {source}")
            print(
                f"    {stats['original_tokens']}t -> {stats['compressed_tokens']}t ({stats['ratio']:.1f}x)"
            )
            print(f"    {compressed}")
            print()

    # Store compressed versions (unless dry-run)
    if not args.dry_run:
        try:
            comp_col = client.get_or_create_collection("brain_compressed")
            for doc_id, compressed, meta, stats in compressed_entries:
                comp_meta = dict(meta)
                comp_meta["compression_ratio"] = round(stats["ratio"], 1)
                comp_meta["original_tokens"] = stats["original_tokens"]
                comp_col.upsert(
                    ids=[doc_id],
                    documents=[compressed],
                    metadatas=[comp_meta],
                )
            print(
                f"  Stored {len(compressed_entries)} compressed drawers in 'brain_compressed' collection."
            )
        except Exception as e:
            print(f"  Error storing compressed drawers: {e}")
            sys.exit(1)

    # Summary
    ratio = total_original / max(total_compressed, 1)
    orig_tokens = Dialect.count_tokens("x" * total_original)
    comp_tokens = Dialect.count_tokens("x" * total_compressed)
    print(f"  Total: {orig_tokens:,}t -> {comp_tokens:,}t ({ratio:.1f}x compression)")
    if args.dry_run:
        print("  (dry run -- nothing stored)")


WELCOME_BANNER = r"""
═══════════════════════════════════════════════════════════════════
  AI Brain for India Lawyers · v0.1.2

  🙏 चलिए शुरू करें, अधिवक्ता जी
  चला सुरू करूया, वकील साहेब
  Let's begin, Advocate.
═══════════════════════════════════════════════════════════════════
  Built on Brain (MIT — github.com/brain/brain)
  Published by Wolfgang_rush · ₹0 forever · your data stays here
  https://github.com/Wolfgangrush/ai-law-firm-india
═══════════════════════════════════════════════════════════════════
"""


def _print_welcome():
    """Print welcome banner. Called when running with no arguments."""
    print(WELCOME_BANNER)
    print(
        "  This is YOUR practice OS. No cloud. No subscription.\n"
        "  Built by an Indian advocate, for Indian advocates.\n"
    )
    print("  Quick start:")
    print("    ailawfirm-india init <your-projects-dir>   # one-time setup")
    print("    ailawfirm-india mine <your-projects-dir>   # ingest your matters")
    print('    ailawfirm-india search "<query>"           # find anything\n')
    print("  Read GETTING_STARTED.md (also GETTING_STARTED_HINDI.md, _MARATHI.md)")
    print("  for a layman-friendly tour.\n")


def main():
    # Show welcome banner when no args (i.e., user just typed `ailawfirm-india`)
    if len(sys.argv) == 1:
        _print_welcome()
        sys.exit(0)

    parser = argparse.ArgumentParser(
        description="AI Brain India — practice OS for Indian solo advocates. "
        "Built on Brain (MIT). Published by Wolfgang_rush.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--palace",
        default=None,
        help="Where the palace lives (default: from ~/.ailawfirm-india/config.json or ~/.ailawfirm-india/palace)",
    )

    sub = parser.add_subparsers(dest="command")

    # init
    p_init = sub.add_parser("init", help="Detect rooms from your folder structure")
    p_init.add_argument("dir", help="Project directory to set up")
    p_init.add_argument(
        "--yes", action="store_true", help="Auto-accept all detected entities (non-interactive)"
    )

    # mine
    p_mine = sub.add_parser("mine", help="Mine files into the palace")
    p_mine.add_argument("dir", help="Directory to mine")
    p_mine.add_argument(
        "--mode",
        choices=["projects", "convos"],
        default="projects",
        help="Ingest mode: 'projects' for code/docs (default), 'convos' for chat exports",
    )
    p_mine.add_argument("--wing", default=None, help="Wing name (default: directory name)")
    p_mine.add_argument(
        "--agent",
        default="brain",
        help="Your name — recorded on every drawer (default: brain)",
    )
    p_mine.add_argument("--limit", type=int, default=0, help="Max files to process (0 = all)")
    p_mine.add_argument(
        "--dry-run", action="store_true", help="Show what would be filed without filing"
    )
    p_mine.add_argument(
        "--extract",
        choices=["exchange", "general"],
        default="exchange",
        help="Extraction strategy for convos mode: 'exchange' (default) or 'general' (5 memory types)",
    )

    # search
    p_search = sub.add_parser("search", help="Find anything, exact words")
    p_search.add_argument("query", help="What to search for")
    p_search.add_argument("--wing", default=None, help="Limit to one project")
    p_search.add_argument("--room", default=None, help="Limit to one room")
    p_search.add_argument("--results", type=int, default=5, help="Number of results")

    # compress
    p_compress = sub.add_parser(
        "compress", help="Compress drawers using Entity-Aliasing Dialect (~30x reduction)"
    )
    p_compress.add_argument("--wing", default=None, help="Wing to compress (default: all wings)")
    p_compress.add_argument(
        "--dry-run", action="store_true", help="Preview compression without storing"
    )
    p_compress.add_argument(
        "--config", default=None, help="Entity config JSON (e.g. entities.json)"
    )

    # wake-up
    p_wakeup = sub.add_parser("wake-up", help="Show L0 + L1 wake-up context (~600-900 tokens)")
    p_wakeup.add_argument("--wing", default=None, help="Wake-up for a specific project/wing")

    # split
    p_split = sub.add_parser(
        "split",
        help="Split concatenated transcript mega-files into per-session files (run before mine)",
    )
    p_split.add_argument("dir", help="Directory containing transcript files")
    p_split.add_argument(
        "--output-dir",
        default=None,
        help="Write split files here (default: same directory as source files)",
    )
    p_split.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be split without writing files",
    )
    p_split.add_argument(
        "--min-sessions",
        type=int,
        default=2,
        help="Only split files containing at least N sessions (default: 2)",
    )

    # status
    sub.add_parser("status", help="Show what's been filed")

    # update — pull latest firm code from upstream (apt-upgrade style)
    p_update = sub.add_parser(
        "update",
        help="Pull the latest firm code, skills, and prompts from upstream (matter data is NEVER touched)",
    )
    p_update.add_argument(
        "--quiet", "-q", action="store_true", help="suppress pip output (errors still print)"
    )

    p_connect = sub.add_parser(
        "connect-local",
        help="One-command setup: install Ollama + download Qwen3 + write config (local-AI, zero cloud)",
    )
    p_connect.add_argument("--yes", "-y", action="store_true", help="skip confirmation prompts")
    p_connect.add_argument("--model", help="override the recommended model (e.g. qwen3:7b)")

    # lite — opt-in low-RAM-Mac mode (defers .docx, skips MCP autostart)
    p_lite = sub.add_parser(
        "lite",
        help="Toggle lite mode for low-RAM Macs (defers .docx, skips MCP autostart). Opt-in.",
    )
    p_lite.add_argument(
        "action",
        nargs="?",
        choices=["on", "off"],
        default=None,
        help="omit to show current state",
    )

    # doctor — diagnostic of thermal/RAM state
    sub.add_parser(
        "doctor",
        help="Diagnose thermal/RAM state — charger · lite mode · pandoc · memory pressure",
    )

    # finalize — batch-generate .docx for a matter folder
    p_finalize = sub.add_parser(
        "finalize",
        help="Batch-generate .docx for every .md in a matter folder (used with lite mode)",
    )
    p_finalize.add_argument("matter", help="Matter folder path")
    p_finalize.add_argument(
        "--max-cpu",
        type=int,
        default=80,
        help="Soft CPU cap %% (informational; pandoc is nice'd) — default 80",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    from .connect_local import cmd_connect_local

    dispatch = {
        "init": cmd_init,
        "mine": cmd_mine,
        "split": cmd_split,
        "search": cmd_search,
        "compress": cmd_compress,
        "wake-up": cmd_wakeup,
        "status": cmd_status,
        "connect-local": cmd_connect_local,
        "update": cmd_update,
        "lite": cmd_lite,
        "doctor": cmd_doctor,
        "finalize": cmd_finalize,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
