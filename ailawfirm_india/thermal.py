"""Thermal hygiene helpers — opt-in lite mode for low-RAM Macs (M1/M2 Air 8GB).

Lite mode defers the per-draft .docx generation (pandoc is the biggest single
CPU consumer per drafting turn on a fanless 8GB Mac) and skips MCP-server
autostart. The .docx files are still produced — just batched later via
`ailawfirm-india finalize <matter>`. Same content, same fidelity.

Lite mode is OPT-IN. Default behaviour is unchanged.
"""

import os
import shutil
import subprocess
from pathlib import Path

LITE_FLAG = Path.home() / ".ailawfirm-india" / "lite.flag"


def is_lite_mode() -> bool:
    """Return True if lite mode is enabled (env var OR flag file)."""
    if os.environ.get("AILAWFIRM_LITE") == "1":
        return True
    return LITE_FLAG.exists()


def set_lite_mode(on: bool) -> None:
    """Toggle the lite-mode flag file."""
    LITE_FLAG.parent.mkdir(parents=True, exist_ok=True)
    if on:
        LITE_FLAG.touch()
    elif LITE_FLAG.exists():
        LITE_FLAG.unlink()


def _safe_run(cmd, timeout=3):
    """Run a system command with a timeout. Return stdout or empty on failure."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return result.stdout
    except Exception:
        return ""


def check_charger() -> dict:
    """Check whether the Mac is on AC power."""
    out = _safe_run(["pmset", "-g", "batt"])
    if not out:
        return {"plugged": None, "raw": "pmset unavailable"}
    plugged = "AC Power" in out
    return {"plugged": plugged, "raw": out.strip()}


def memory_pressure_summary() -> str:
    """Return a short summary of vm_stat output."""
    out = _safe_run(["vm_stat"])
    if not out:
        return "vm_stat unavailable"
    # Pull the headline lines only (free, active, wired, compressed)
    keep = ("Pages free", "Pages active", "Pages wired", "Pages occupied by compressor")
    lines = [ln for ln in out.splitlines() if any(k in ln for k in keep)]
    return "\n  ".join(lines) if lines else "vm_stat parsed empty"


def run_doctor() -> int:
    """Print diagnostic state. Returns 0 always (informational only)."""
    print("\n  AI Brain India — doctor")
    print("  " + "-" * 50)

    # Lite mode
    print(f"  Lite mode:           {'ON' if is_lite_mode() else 'OFF'}")

    # Charger
    chg = check_charger()
    if chg["plugged"] is True:
        chg_label = "plugged in (AC)"
    elif chg["plugged"] is False:
        chg_label = "on battery"
    else:
        chg_label = "unknown"
    print(f"  Charger:             {chg_label}")

    # pandoc
    pandoc_path = shutil.which("pandoc")
    print(
        f"  pandoc:              {'present at ' + pandoc_path if pandoc_path else 'MISSING — brew install pandoc'}"
    )

    # Python
    import sys

    print(f"  Python:              {sys.version.split()[0]}")

    # Memory pressure
    print("  Memory (vm_stat):")
    print(f"    {memory_pressure_summary()}")

    # Hint
    if not is_lite_mode():
        print("\n  💡 On a fanless 8GB Mac and seeing heat / auto-shutdown?")
        print("     Try:  ailawfirm-india lite on")
        print("           — defers .docx generation, skips MCP autostart")
        print("           — batch-generate via:  ailawfirm-india finalize <matter>")
    print()
    return 0
