# Running on a Low-RAM Mac (8GB M1 / M2 Air)

This guide is for advocates running AI Brain — India on a fanless 8GB Mac (M1 Air, M2 Air, base Mac mini). If your laptop runs hot, throttles, or shuts down during long drafting sessions, the playbook below helps.

**Default firm behaviour is unchanged.** Everything in this guide is opt-in.

---

## Why fanless 8GB Macs need a different playbook

- **Fanless** → passive cooling only. The chip can hit thermal limits during sustained workloads.
- **8GB RAM** → constant memory pressure when Chrome / Safari / web apps are open alongside terminal work. macOS pages to SSD, which generates more heat.
- **Combined power + thermal envelope** → at low battery state-of-charge, the firmware is more likely to trigger an emergency shutdown if CPU load + battery internal resistance push the envelope.

This is normal hardware behaviour for the class. It's not a hardware fault, and battery health usually stays fine. The fix is workflow discipline, not new hardware.

---

## The 4-step workflow checklist

Before any long drafting session:

### 1. Plug in the charger

Battery + sustained CPU load is what trips the shutdown. AC power removes that variable.

### 2. Close browser tabs

Chrome and Safari tabs are the largest single RAM consumers on most setups. 10 tabs across both browsers can eat 4-6 GB on their own, which leaves little headroom for the AI tool and your drafting work.

Open Activity Monitor (`Cmd+Space` → "Activity Monitor"), switch to the Memory tab, sort by Memory column descending, and quit anything 1 GB+ that you're not actively using.

### 3. One AI tool at a time

If you're using Claude (Pro app or Code), don't simultaneously run Gemini CLI, Gemini web, or other LLM tools. Switch between them sequentially.

Gmail and Google Drive web tabs also count — keep one open at a time when drafting matters.

### 4. Enable lite mode

```
ailawfirm-india lite on
```

This is the firm-side fix. Details below.

---

## What lite mode does

When you turn lite mode ON, two things change for the rest of your sessions:

### A. Per-draft `.docx` generation is deferred

Normally the firm produces a paired `.md` + `.docx` for every drafted document, in the same tool-call window. `pandoc` (the binary that does `.md` → `.docx` conversion) runs as a subprocess every time.

On a fanless 8GB Mac, that pandoc subprocess is the single largest CPU consumer per drafting turn. Across a long session that's dozens of CPU spikes, each contributing to heat.

In lite mode, the firm produces the `.md` only. The `.docx` is generated later in one batched run via `finalize` (see below). Same content, same pandoc, same fidelity — just batched.

### B. MCP-server autostart is skipped

If the firm would otherwise auto-start an MCP server process at session start, lite mode skips that. You can still invoke MCP-server features manually if you need them. (Most advocates using Claude Pro app or Claude Code don't use MCP at all — this is a no-op for them.)

---

## Generating `.docx` at end of session

When you finish drafting and want the `.docx` files (for filing in court or emailing to clients), run:

```
ailawfirm-india finalize ~/Desktop/<your-firm>/<matter-folder>
```

This walks the matter folder, finds every `.md` file, and generates the paired `.docx` via `nice`'d pandoc — one batched CPU burst instead of dozens of per-keystroke spikes. Files that already have an up-to-date `.docx` are skipped.

You can pass `--max-cpu N` (informational) to remind yourself to keep load deprioritised. The pandoc binary itself doesn't honour a CPU cap, but `nice -n 10` lowers process priority so other work stays responsive.

---

## Diagnosing in real-time

If the laptop feels hot or slow, run:

```
ailawfirm-india doctor
```

You'll see:

- **Lite mode** — ON or OFF
- **Charger** — plugged in (AC) or on battery
- **pandoc** — present at path, or MISSING (install via `brew install pandoc`)
- **Python** version
- **Memory pressure** — `vm_stat` summary (pages free, active, wired, compressed)

The output suggests one concrete next move (plug in / enable lite / install pandoc / etc).

---

## Quality is unchanged

The single most important question for any opt-in toggle: does it compromise output?

**No.** Here's why:

| Aspect | Default mode | Lite mode | Quality delta |
|---|---|---|---|
| Claude / Gemini draft text | Same prompt, same skill, same output | Same | None |
| Markdown fidelity | `.md` written verbatim | `.md` written verbatim | None |
| `.docx` fidelity | pandoc converts per-draft | pandoc converts at `finalize` (same binary, same flags) | None — pandoc is deterministic for the same input |
| Audience fit (filing / email) | `.docx` ready per draft | `.docx` ready after `finalize` (one extra command at session end) | Workflow delta, not quality |

The trade-off is purely workflow: you run `finalize` once per session instead of getting `.docx` automatically per draft. The `.docx` files themselves are bit-identical to what default-mode would have produced.

---

## Cross-LLM parity (Gemini users)

Gemini users get the same behaviour via slash-commands:

- `/lite on` — enable lite mode
- `/lite off` — disable
- `/lite` — check current state
- `/doctor` — diagnose
- `/finalize <matter>` — batch-generate `.docx`

These mirror the `ailawfirm-india lite | doctor | finalize` CLI commands one-for-one. Per the publisher's cross-LLM parity policy, Claude skills and Gemini commands always ship in lockstep.

---

## Turning lite mode off

If you upgrade to a higher-RAM machine later or just want default behaviour back:

```
ailawfirm-india lite off
```

Default per-draft `.md` + `.docx` pairing resumes immediately.

---

## When lite mode isn't enough

If you've enabled lite mode, plugged in the charger, closed browser tabs, and the laptop still shuts down during sessions — the bottleneck is not firm-side. Open an issue on the GitHub repository with:

1. Output of `ailawfirm-india doctor` at the time of slowdown
2. Approximate moment of shutdown (e.g., "during a long draft, ~15 min in")
3. Activity Monitor screenshot if possible

Workflow-discipline and lite mode together cover the common cases. Cases beyond that need targeted diagnosis.
