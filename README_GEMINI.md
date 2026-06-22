# 🇮🇳 AI Brain for India Lawyers — **Gemini CLI Port**

> The same firm you already know, now running on Google's Gemini CLI instead of (or alongside) Claude Code. **Same 7 specialists. Same Python backbone. Same BCI Rule 36 + DPDP firewall. Different LLM brain.**

**Version:** 0.1.1 · **Gemini port:** 2026-05-24 · **License:** MIT · **Publisher:** [Wolfgang_rush](https://github.com/Wolfgangrush)

---

## What this port adds

This folder now contains a `.gemini/` directory alongside the existing `.claude/`:

```
ai-law-firm-india-main/
├── .claude/                         ← Claude Code skills (unchanged)
│   └── skills/
│       ├── wake/SKILL.md
│       └── retrospective/SKILL.md
├── .gemini/                         ← NEW · Gemini CLI commands
│   └── commands/
│       ├── wake.toml
│       ├── retrospective.toml
│       ├── receptionist.toml         · 🧠 brain
│       ├── matter.toml               · 📂 Matter Manager
│       ├── citation.toml             · 📜 Citation Clerk
│       ├── court.toml                · 🏛️ Court Registrar
│       ├── drafting.toml             · ✍️ Drafting Assistant
│       ├── compliance.toml           · 🛡️ Compliance Officer
│       └── deadline.toml             · 📅 Deadline Tracker
├── GEMINI.md                        ← NEW · Gemini hierarchical context (loaded automatically)
├── README_GEMINI.md                 ← NEW · This file
└── ailawfirm_india/                  ← Python backbone (unchanged)
```

**Nothing in the existing codebase was modified.** The Gemini port is additive only. Both `.claude/` (Claude Code) and `.gemini/` (Gemini CLI) coexist — choose whichever brain you want for any session.

---

## Why Gemini CLI specifically

Three honest reasons an Indian advocate might choose Gemini over Claude or Ollama:

| Reason | Detail |
|---|---|
| **Long PDF reads** | Gemini's 1M-token context window handles full case files, multi-volume paper books, voluminous chargesheets / counter-affidavits without chunking |
| **Cheaper than Claude** | Gemini paid tier typically lands ₹500-2000/mo for moderate use vs Claude's ₹1500-5000/mo |
| **Already in the ecosystem** | If you already use Google Workspace / Drive / Sheets, the Gemini API ties in cleanly |

**Caveat — privacy:** Gemini **free tier uses prompts for training** by Google's stated policy. Gemini **paid tier does NOT** (per [Google AI Studio terms](https://ai.google.dev/gemini-api/terms)). For client data → **paid tier only**, or use local Ollama via the existing `ailawfirm-india` CLI.

See [MODEL_SETUP.md](MODEL_SETUP.md) §Option D for the full Gemini privacy table.

---

## Install — 4 steps

### Step 1 — Install Gemini CLI (one-time)

**Requires Node.js 20+** ([download](https://nodejs.org/)).

```bash
npm install -g @google/gemini-cli
```

Verify:
```bash
gemini --version
```

(Alternative installs: `npx @google/gemini-cli` for no-install, or `brew install gemini-cli` if Homebrew has it on your version of macOS.)

### Step 2 — Set your Gemini API key

Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).

**For client work → set up paid billing FIRST.** Free tier sends your prompts into training.

```bash
export GEMINI_API_KEY="your-api-key-here"
```

Persist this in `~/.zshrc` (Mac/Linux) or PowerShell profile (Windows) so it survives terminal restarts.

### Step 3 — Install the Python backbone (one-time, if not already done)

The Gemini commands call into the same `ailawfirm_india` Python package as the Claude Code port:

```bash
pip install -e .
```

Run from this folder (the one containing `pyproject.toml`).

### Step 4 — Launch Gemini CLI from this folder

```bash
cd "ai-law-firm-india-main"
gemini
```

Gemini will automatically load `GEMINI.md` from this folder (and from your home `~/.gemini/GEMINI.md` if you have a global one). The 9 custom commands in `.gemini/commands/` are now available as slash commands.

---

## Use — first session

Once inside the `gemini` REPL:

```
> /wake
```

You should see the readiness banner: leak-check PASS, 25 High Courts mapped, 7 specialists online.

Now ask anything in plain English (the brain auto-routes), or invoke a specialist directly with a slash command:

| Plain English (auto-routed via `/receptionist` or inline) | Direct slash command |
|---|---|
| `tell me about your High Court` | `/court your High Court` |
| `validate AIR 1973 SC 1461` | `/citation AIR 1973 SC 1461` |
| `is "best advocate in Mumbai" Rule 36 compliant?` | `/compliance "best advocate in Mumbai"` |
| `draft a writ petition Art 226 skeleton` | `/drafting writ petition Art 226` |
| `limitation for Section 138 NI Act` | `/deadline Section 138 NI Act` |
| `summarise my next hearing matter` | `/matter [paste matter sheet]` |
| `classify this for me: [free text]` | `/receptionist [free text]` |

At the end of the session:

```
> /retrospective
```

A timestamped session summary is written to `~/.ailawfirm-india/sessions/session_YYYY-MM-DD_HHMM_gemini.md` — the firm's institutional memory carries forward.

---

## The 9 commands at a glance

| Command | Specialist | What it does |
|---|---|---|
| `/wake` | Receptionist | Boot the firm. 2-pass leak-check + jurisdiction state |
| `/retrospective` | Receptionist | End-of-session save. 2-pass leak-check + session summary |
| `/receptionist [text]` | 🧠 Brain | Classify intent, respond in matching specialist's voice |
| `/matter [text]` | 📂 Matter Manager | Active case context (v0.1 = structures advocate-supplied input) |
| `/citation [text]` | 📜 Citation Clerk | Validate AIR / SCC / SCC OnLine format via Python backend |
| `/court [text]` | 🏛️ Court Registrar | Jurisdiction · pecuniary · territorial · procedural rules |
| `/drafting [text]` | ✍️ Drafting Assistant | Skeleton for petition / reply / affidavit / etc. |
| `/compliance [text]` | 🛡️ Compliance Officer | BCI Rule 36 two-prong + DPDP Act 2023 firewall |
| `/deadline [text]` | 📅 Deadline Tracker | Limitation Act 1963 high-frequency anchors + computation rules |

---

## Privacy — the honest version, again

| What you are running | Where your data goes |
|---|---|
| The Python backbone (`ailawfirm_india`) + `~/.ailawfirm-india/` data | **Your laptop only.** SQLite + ChromaDB. Never leaves. |
| `GEMINI.md` + `.gemini/commands/*.toml` (this port) | **Your laptop only.** Loaded by Gemini CLI from disk. |
| **What you type into the `gemini` prompt** | **Google's Gemini infrastructure (USA + globally).** Paid tier: NOT used for training. Free tier: MAY be used for training. |
| **What Gemini types back to you** | Returned over the network from Google's servers. |

**Decision rule for client data:**

- ✅ **Local Ollama** (via the existing `ailawfirm-india` CLI, `"ai_provider": "ollama"`) → real client matters, attorney-client privileged research, DPDP-sensitive material
- ✅ **Gemini paid tier** (this port) → drafting templates, public statutes, DPDP/BNS/CPC study, generic writing, LinkedIn-post compliance checks (no real client names)
- ❌ **Gemini free tier** → never for any work that could be construed as confidential. Training-data inclusion is the default on free tier.
- ❌ **Any cloud LLM** for any client data without client consent + verified data-processing agreement → breach of **BCI Rule 17 + Advocates Act §35**.

This is a non-negotiable line. The implementation can flex by income (see [MODEL_SETUP.md](MODEL_SETUP.md) §Tier 1-4 honest tiered guide); the principle does not.

---

## What the Gemini port does NOT do

- Does **NOT** modify any existing file in the repo. Pure additive.
- Does **NOT** disable, replace, or compete with the Claude Code port. Both coexist.
- Does **NOT** read or write to the local memory layer or any other personal data store.
- Does **NOT** access your personal diary, knowledge graph, or self-assessment data.
- Does **NOT** route around your local-Ollama setting in `~/.ailawfirm-india/config.json`. If you want the bundled CLI to use Ollama, that CLI honours its own config independently. This Gemini port is a SEPARATE LLM brain you invoke deliberately by running `gemini`.

---

## Troubleshooting

### `gemini: command not found`
Node 20+ installed? `npm install -g @google/gemini-cli` succeeded? Restart terminal.

### Custom commands not appearing
Make sure you launched `gemini` from inside the `ai-law-firm-india-main/` folder (the one containing `.gemini/`). Project-level commands need the working directory to match.

### `python3: command not found` inside a Gemini command
The Gemini commands call `python3` via shell injection. Make sure Python 3.10+ is on `PATH` and `ailawfirm_india` is installed (`pip install -e .` from this folder).

### `ailawfirm_india` import errors
```bash
pip install -e .
python3 -c "import ailawfirm_india; print(ailawfirm_india.__file__)"
```
If the import succeeds, the Gemini commands will find it.

### `GEMINI_API_KEY` errors
Did you `export GEMINI_API_KEY="..."` and is the variable persisted in your shell profile?
```bash
echo $GEMINI_API_KEY
```

### Free tier vs paid tier
Check at [Google AI Studio billing](https://aistudio.google.com/app/billing). If you have not enabled billing, you are on free tier — **do not use for client data**.

---

## Differences from the Claude Code port (for anyone curious)

| Aspect | Claude Code (`.claude/skills/`) | Gemini CLI (`.gemini/commands/`) |
|---|---|---|
| File format | Markdown with YAML frontmatter (`SKILL.md`) | TOML (`description = ` + `prompt = """..."""`) |
| Context-loading file | `CLAUDE.md` (auto-loaded) | `GEMINI.md` (auto-loaded) |
| Allowed-tools declaration | Frontmatter `allowed-tools:` field | Implicit; Gemini CLI sandbox controls available tools |
| Shell injection | Bash tool calls written inline | `!{...}` shell injection inside the prompt body |
| Argument passing | Variable depending on invocation | `{{args}}` placeholder substituted at call time |
| Discovery | `claude` reads `.claude/` automatically | `gemini` reads `.gemini/` automatically |

Both ports point at the **same** Python backbone (`ailawfirm_india/`) and the **same** data store (`~/.ailawfirm-india/`). The only difference is which LLM is the brain on top.

---

## Roadmap for the Gemini port (honest)

- **v0.1.x — DONE** — 9 commands · GEMINI.md context · 2-pass leak-check · BCI Rule 36 + DPDP firewall · Python-backbone integration
- **v0.2** *(when the main repo's v0.2 lands)* — real statute text wired into `/drafting` + `/deadline` · full Limitation Act 1963 Schedule · matter store in `/matter`
- **v0.3+** — Wolfgang_rush drafting plugin integration · cause-list scraping · calendar sync

If the main repo `ailawfirm_india/` upgrades, this Gemini port inherits the upgrade automatically (the TOML commands call the same Python functions).

---

## ⚖️ Same compliance posture as the main repo

This Gemini port is **assistive legal-work infrastructure**, not autonomous decision-making software. Same Supreme Court e-Committee alignment as the main repo — see [README.md](README.md) §Compliance posture.

> *"AI and digital tools must be used as supportive instruments and should not be allowed to override judicial reasoning."*
> — **Justice Rajesh Bindal**, Judge, Supreme Court of India

**Every output from this tool — whether the brain is Claude, Gemini, or Ollama — must be advocate-owned and human-verified before any client use or filing.**

---

## ⚠️ Third-party CLI tools and IDEs — user assumes all risk

(Reproduced from [MODEL_SETUP.md](MODEL_SETUP.md) for visibility.)

If you integrate this Software with **any third-party AI service, CLI tool, or AI-assisted IDE** — including **Google Gemini API · Gemini CLI** — you do so **at your own risk** and under the terms of service of that third-party tool.

The publisher (Wolfgang_rush · Rushikesh R. Mahajan):

- Does **NOT** recommend any specific third-party tool, including Gemini CLI
- Does **NOT** receive any compensation, referral fee, or benefit from Google or any other third-party tool's adoption
- Does **NOT** verify any third-party tool's privacy posture, security, or compliance with your jurisdiction's law
- Accepts **NO** responsibility for your choice of third-party tooling
- Accepts **NO** responsibility for any data leakage, confidentiality breach, professional-conduct violation, regulatory non-compliance, or any other harm resulting from your use of third-party tools alongside this Software

**You are solely responsible** for:
- Reading Gemini's privacy policy and terms of service before connecting it
- Ensuring compliance with all confidentiality rules, data-protection laws, sectoral regulations, and bar conduct rules that apply to your practice
- Obtaining client consent where required before routing client data through Gemini
- Verifying that Gemini does not retain, train on, or share your queries in ways that breach your professional obligations
- Managing your `GEMINI_API_KEY` securely (do not commit it to version control; use environment variables)
- Independently verifying any output produced by Gemini before client-facing use

---

## 📞 Support

- **Issues with this Gemini port:** open an issue at https://github.com/Wolfgangrush/ai-law-firm-india/issues with `[gemini-port]` label
- **Issues with Gemini CLI itself:** that's a Google product · see [Gemini CLI GitHub](https://github.com/google-gemini/gemini-cli) (or whichever upstream is current)
- **Issues with the Python backbone:** the same as the main repo

---

`चलिए शुरू करें · चला सुरू करूया · Let's begin.` 🙏
