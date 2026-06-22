# 🙏 Welcome, Adv. _____ — your AI Brain starts here

You don't need to be a programmer. You don't need to buy a Mac. You don't need a subscription. You need a Windows laptop or a Mac, an internet connection for setup, and 30 minutes.

If you can copy-paste, you can run this.

> **Hindi (हिन्दी):** [GETTING_STARTED_HINDI.md](GETTING_STARTED_HINDI.md)
> **Marathi (मराठी):** [GETTING_STARTED_MARATHI.md](GETTING_STARTED_MARATHI.md)
> **Windows install:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md)
> **Mac install:** [MAC_INSTALL.md](MAC_INSTALL.md)
> **Connecting an AI model:** [MODEL_SETUP.md](MODEL_SETUP.md)

---

## ✨ What this is, in one paragraph

A free tool that turns your laptop into a small private law office assistant. It remembers your matters (every case file, every party, every order, every hearing date). It parses Indian legal citations (AIR · SCC · SCC OnLine). It tells you which court has jurisdiction over what. It flags BCI Rule 36 risks (so you don't accidentally solicit work). It runs **on your own computer** — no cloud, no upload, no third party reads your client data. It's open-source (MIT licensed). You own everything you put into it.

## 💛 Why a solo Indian advocate should care

The big firms have armies of associates to check citations, manage matters, draft replies. You don't. You have your own brain and a notebook. This is your second brain.

- **You forget less.** Months-old matter context comes back instantly.
- **You miss fewer deadlines.** Hearing dates and limitation periods are tracked, not remembered.
- **You stay BCI-Rule-36 safe.** A built-in firewall checks language for solicitation/advertising risk before you publish anything.
- **You save money.** Manupatra is ₹15,000+/year. LawNet is more. This is ₹0.
- **You stay private.** Your client matters NEVER leave your laptop unless you choose to send them somewhere.
- **You can scale.** When you hire your first associate, switch from `--mode solo` to `--mode firm` — same tool, same data, more users.

## 🧠 What's inside (in plain English)

Think of it as 7 specialists who live inside your terminal:

1. **The Receptionist (the "brain")** — listens to what you say, figures out who you need (a citation check? a court lookup? a deadline calculation?), then calls the right specialist. You never have to memorize commands.
2. **The Citation Clerk** — recognizes AIR 1973 SC 1461 and similar Indian citation formats. Tells you if the citation is valid.
3. **The Court Registrar** — knows the courts. Tell it "your High Court" and it tells you the jurisdiction, the procedural rules, what kinds of matters it hears.
4. **The Matter Manager** — holds your active case files. Each matter has its own memory (parties, prayers, hearings, orders, drafts).
5. **The Drafting Assistant** — works with the Wolfgang_rush drafting plugins (separate, optional) to produce clean drafts. v0.1 has the connection; the actual drafting templates come with v0.2.
6. **The Compliance Officer** — watches for BCI Rule 36 violations (no soliciting, no advertising), DPDP Act compliance issues, and other ethics flags. Catches you before you make a mistake.
7. **The Deadline Tracker** — limitation periods, hearing dates, filing deadlines (v0.2 will handle the full Limitation Act 1963 schedule).

The Receptionist is the only one you talk to. The Receptionist talks to the others. You never have to learn 7 different tools.

## 🚀 Your first 30 minutes (the quick start)

### Step 1 — Install Python (one-time, 5 minutes)
- **Mac:** [MAC_INSTALL.md](MAC_INSTALL.md) — has the exact commands
- **Windows:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md) — uses PowerShell, screenshots included

### Step 2 — Install AI Brain India (one command)

After Python is installed, open Terminal (Mac) or PowerShell (Windows) and paste:

```
pip install git+https://github.com/Wolfgangrush/ai-law-firm-india.git
```

Wait for it to finish (1-2 minutes). It will download about 200 MB. You only do this ONCE.

### Step 3 — Connect an AI brain (10 minutes)

The tool itself is just a structured database + brain layer. To get the AI part working — drafting, smart conversation, reasoning — you connect it to an AI model.

**Three choices, in order of recommendation:**

| Choice | Cost | Privacy | Best for |
|---|---|---|---|
| 🥇 **Run a local model (Ollama + Qwen3)** | ₹0 forever | 🟢 Perfect — nothing leaves your laptop | **Anyone handling client matters** |
| 🥈 **DeepSeek API** | ~₹80-200/month for moderate use | ⚠️ Good but NOT automatic — you must opt-out of training data (see MODEL_SETUP.md) | Drafting templates · research summaries · NON-client-data work |
| 🥉 **Claude API / Gemini API** | ~₹1500-5000/month | 🟢 Strong (enterprise tier) | Heavy daily users, after first paid engagement |

See [MODEL_SETUP.md](MODEL_SETUP.md) for the exact setup steps for each.

### Step 4 — Your first interaction

```
ailawfirm-india
```

You'll see this:

```
═══════════════════════════════════════════════════════════════════
  AI Brain for India Lawyers · v0.1.1
  चलिए शुरू करें, अधिवक्ता जी 🙏
═══════════════════════════════════════════════════════════════════
  Built on the local memory layer (MIT — github.com/brain/brain)
  Published by Wolfgang_rush · ₹0 forever · your data stays here
═══════════════════════════════════════════════════════════════════

Type 'help' for a tour, or just ask a question.
>
```

Try these:
```
> tell me about your High Court
> validate AIR 1973 SC 1461
> check this language: "Best advocate in Mumbai"
> what's the limitation period for a money suit?
```

The Receptionist (brain) figures out what you need and routes to the right specialist.

## 🛡️ Privacy promises (the honest version)

**What we guarantee (the tool itself):**
- Your matters, clients, drafts, and notes stay on your laptop. They are NEVER uploaded to any cloud by this tool.
- All data is in a folder you control: `~/.ailawfirm-india/` (Mac) or `C:\Users\<you>\.ailawfirm-india\` (Windows).
- You can copy this folder to a USB drive and have a complete backup of your practice in 5 seconds.
- Source code is MIT licensed — you can read every line, audit anything, modify anything.

**What we cannot guarantee (the AI model you connect):**
- If you use a cloud AI API (DeepSeek · Claude · Gemini), the queries you send to that API leave your laptop and go to their servers.
- Each provider has their own privacy policy. We've summarized the honest version in [MODEL_SETUP.md](MODEL_SETUP.md).
- For genuine client confidentiality, use the **local Ollama model option**. Nothing leaves your laptop. Slower than cloud, but private.

**BCI Rule 36 + DPDP compliance:**
- The Compliance Officer specialist checks your language for solicitation/advertising risk BEFORE you publish anything (LinkedIn posts, website copy, brochures).
- For DPDP Act compliance: client data stays local by default. If you choose to use a cloud AI, you're responsible for ensuring DPDP-compliance terms (we can't enforce them on you).

## 📁 Where everything lives

After install, the tool creates:

```
~/.ailawfirm-india/                     ← Your data home
├── palace/                             ← All matter / client / citation memory
├── config.json                         ← Your settings (which AI model, etc.)
└── people_map.json                     ← Optional alias system for clients/parties
```

Back this up with: `cp -R ~/.ailawfirm-india ~/Dropbox/ailawfirm-india-backup` (Mac/Linux) or use Windows File Explorer to copy `C:\Users\<you>\.ailawfirm-india\` to OneDrive/Dropbox.

## 🆘 If something breaks

1. **First check:** is your AI model working? Run `ailawfirm-india doctor` (v0.2). For v0.1, check your API key in `~/.ailawfirm-india/config.json`.
2. **Second check:** GitHub issues at https://github.com/Wolfgangrush/ai-law-firm-india/issues
3. **For peer help:** Indian Lawyers / Wolfgang_rush LinkedIn community (announced in the launch post).

This is v0.1 — bootstrap version. v0.2 (real statute text) and v0.3 (firm mode for multi-advocate practices) are coming.

## 🙏 Credits

- **Architecture engine:** a local memory architecture — the highest-scoring open-source AI memory system ever benchmarked. MIT licensed. All credit to the the local memory layer authors.
- **Publisher:** [Wolfgang_rush](https://github.com/Wolfgangrush)
- **Author:** Rushikesh Mahajan, Advocate (your High Court Bench)
- **Inspired by:** every solo advocate in India who's worked late on a Friday checking a citation by hand, looking at a faded handwritten cause list, trying to remember which date the next hearing is.

If this saves you an hour a week, the tool has paid for itself a thousand times over.

`Sat Sri Akal · Jai Shri Krishna · Bismillah · Namaste · Vanakkam — every dialect of "let's begin." This is yours now.`

---

**License:** MIT (inherited from the local memory layer upstream). See LICENSE file.

**Disclaimer:** This tool helps you organize your practice. It does NOT give legal advice. It does NOT replace your professional judgment. Bar Council Rule 36 firewall is built in but YOU remain responsible for compliance. The tool ships AS-IS without warranty.
