# 🤖 AI Model Setup — Honest Privacy Guide

The tool itself stores everything on your laptop. But to do "smart" work (drafting, conversation, reasoning) you connect it to an AI model. **Where that model runs determines your privacy.**

This guide is honest about every option. No marketing fluff. Read before you pick.

> **Hindi summary:** [GETTING_STARTED_HINDI.md](GETTING_STARTED_HINDI.md) §AI brain जोड़ें
> **Marathi summary:** [GETTING_STARTED_MARATHI.md](GETTING_STARTED_MARATHI.md) §AI brain जोडा

---

## 🎯 The honest privacy table

| Option | Where it runs | Who can see your queries | Cost | Best for |
|---|---|---|---|---|
| 🥇 **Ollama + Qwen3 (local)** | Your laptop | ONLY you | ₹0 forever | **Client matters · DPDP-sensitive work · Court drafts** |
| 🥈 **DeepSeek API** | DeepSeek servers (China) | DeepSeek (unless opted-out) | ~₹80-200/mo moderate use | NON-client work · drafting templates · research summaries |
| 🥉 **Claude API** | Anthropic servers (USA) | Anthropic (per their privacy policy) | ~₹1500-5000/mo | Heavy daily users after first paid engagement |
| 🥉 **Gemini API** | Google servers (USA + globally) | Google | ~₹500-2000/mo | Long-PDF reads · large research synthesis |

---

## 🇮🇳 Honest tiered guide — for the Indian advocate who can't afford a 16GB laptop

This section was added in v0.1.1 (May 2026) after community feedback: **the recommendation to use local-only mode assumes you own a 16GB+ RAM laptop. Most Indian solo advocates don't.** Here is the honest tiered guide for cost-constrained users.

### Tier 1 — Local-only on Ollama Qwen3:7b (RECOMMENDED for client work · works on 8GB RAM)

Even on a ₹40k laptop with 8GB RAM, Qwen3:7b runs. Slower than 14b, lower quality, but **private**. This is the right tier for any work that touches client names, addresses, Aadhaar, PAN, GSTIN, case-specific facts, or any DPDP-sensitive personal data.

If you cannot run even 7b on your laptop, see Tier 3 (borrowed compute) before considering cloud.

### Tier 2 — Cloud with Pseudonymisation Gateway (COMING in v0.2 · NOT YET AVAILABLE)

**v0.2 will ship a "Pseudonymisation Gateway"** — a built-in NER pass that replaces all client names, addresses, Aadhaar, PAN, GSTIN, case numbers, phone, email, and dates with placeholders (`[CLIENT_1]`, `[ADDRESS_1]`, `[ID_1]` etc.) BEFORE any data goes to a cloud API. The cloud sees only abstract structure. The tool de-pseudonymises on return.

This makes cloud mode safe for client work — cloud vendor never sees a real name. **Until v0.2 ships, this safety is NOT YET AVAILABLE.** Do not use cloud mode for client work in v0.1.

### Tier 3 — Cloud raw (acceptable for NON-CLIENT work only)

Cloud APIs (DeepSeek opt-out · Gemini API · Groq free · OpenAI · Anthropic) are acceptable for:

- ✅ Studying DPDP / BNS / CPC / Constitutional Law
- ✅ Drafting template clauses with NO real names
- ✅ Public statute summarisation
- ✅ Researching reported case law
- ✅ Generating learning notes
- ✅ Writing OSS contributions
- ✅ Drafting LinkedIn posts
- ✅ Generating practice exam questions

NOT acceptable for:

- ❌ Anything involving a real client name (even initials)
- ❌ Anything involving an active matter's facts
- ❌ Anything involving Aadhaar / PAN / GSTIN / bank details
- ❌ Anything covered by BCI Rule 17 confidentiality
- ❌ Anything covered by Advocates Act §35

### Tier 4 — Banned (for ALL users, ALL income brackets)

Sending raw client data with real names to ANY cloud API — even with opt-out — without a written client consent and a verified data-processing agreement = breach of BCI Rule 17 + Advocates Act §35. This is non-negotiable.

### 🛠️ Hardware-borrowed paths — when you genuinely cannot run Ollama on your own laptop

You DON'T have to own a powerful laptop. Workable substitutes:

**(a) District court advocates' chambers shared workstation** — many chambers have a desktop with adequate specs. Run Ollama there for the 30-90 minutes you need. Confidentiality stays intact (data stays on the chamber machine, never leaves).

**(b) College / law-clinic computers** — if you have access to your law college's library or clinic computer lab (or know a faculty member with access), Ollama runs there. Same confidentiality logic.

**(c) Google Colab free tier (T4 GPU)** — Qwen3:14b runs on Google's free Colab T4. Session-bound. Per Colab's terms, inference workloads on user-uploaded models are not used for training. Setup: 30-minute one-time. After that, paste a Colab URL into the tool's config to route inference there. **Caveat: data passes through Google's infrastructure during the Colab session — if you're paranoid about Google holding even transient access, skip this option.**

**(d) Friend's / colleague's laptop with adequate RAM** — borrow for evening sessions. Carry an Ollama-loaded USB stick (~12GB) so setup is one command. Data stays local to that laptop.

**(e) Affordable hardware-borrow services** — some cyber cafes in Tier-2/Tier-3 cities now offer "high-RAM laptop rental" at ₹100-300/hour. Workable for occasional confidential AI sessions. Verify they don't keep logs.

### 🔑 The principle — does not bend by income

Client data → third party without consent = BCI Rule 17 breach. This applies whether you earn ₹10,000/month or ₹10,00,000/month. The PRINCIPLE is non-negotiable.

The **implementation** can flex by income — Tier 1-3 above are honest options. Choose the tier that matches your work type, not your wallet. Do not let "I can't afford a 16GB laptop" become "I'll just put client data through Gemini." That's the wrong tradeoff.

---

## 🥇 Option A — Ollama + Qwen3 (local, recommended for client work)

### Why this is the best privacy option
- Model runs ON YOUR LAPTOP. Your queries never leave the machine.
- No internet needed after one-time model download.
- No DPDP / BCI Rule 36 concern about third-party data processing.
- Suitable for handling actual client matters, draft pleadings, confidential research.

### Install
**Mac:** `brew install ollama` (or download from https://ollama.com/download/Mac)
**Windows:** Download installer from https://ollama.com/download
**Linux:** `curl -fsSL https://ollama.com/install.sh | sh`

### Download a model (one-time, 10-20 minutes, ~10 GB)
```
ollama pull qwen3:14b
```

Alternative models if you have less storage:
- `ollama pull qwen3:7b` — 4 GB · slightly worse quality, faster
- `ollama pull llama3.3:8b` — 5 GB · Meta's model, decent
- `ollama pull mistral:7b` — 4 GB · good European model

### Connect to AI Brain India
Open `~/.ailawfirm-india/config.json` (Mac) or `C:\Users\YourName\.ailawfirm-india\config.json` (Windows) and add:

```json
{
  "ai_provider": "ollama",
  "ollama_model": "qwen3:14b",
  "ollama_host": "http://localhost:11434"
}
```

Restart `ailawfirm-india`. It now uses local Ollama. **No queries leave your laptop.**

### Tradeoffs (honest)
- Slower than cloud APIs (maybe 2-5x slower depending on your laptop)
- Quality is slightly lower than top cloud models (but improving rapidly)
- Uses laptop battery + RAM during use
- Best on machines with 16 GB+ RAM (will work on 8 GB but tightly)

### Hardware reality check
- MacBook Air M1/M2 8GB: works with `qwen3:7b` (smaller model)
- MacBook Air M2/M3 16GB+: works smoothly with `qwen3:14b`
- Windows laptop with 16GB RAM + dedicated GPU: works well with `qwen3:14b`
- Older Windows laptops (4-8GB RAM, no GPU): use `qwen3:7b` or smaller
- Phone/tablet: not supported for local model (use Option B/C/D)

---

## 🥈 Option B — DeepSeek API (cheap cloud, MANDATORY privacy setup)

### Why solo advocates love DeepSeek
- **Cheapest** capable cloud model right now (~10-20× cheaper than Claude/GPT)
- Anthropic-compatible API (works with Claude Code and similar tools out of the box)
- Strong on agentic / tool-use workloads

### ⚠️ The honest privacy fact (READ BEFORE USING)

DeepSeek's privacy policy says they **may use your API inputs and outputs for service improvement** (training). They offer an opt-out, but it is NOT the default.

**Per DeepSeek's official policy ([source](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html)):**
> *"DeepSeek may use inputs and outputs to a minimal extent to develop or improve services under secure encryption technology processing, strict de-identification rendering, and with irreversibility to identify specific individuals."*

> *"Users can disable the option labeled 'Improve the model for everyone' to reduce the likelihood that their chats will end up in DeepSeek's training datasets."*

**Additional context:** A 2025 security audit found 12,000 live API keys/passwords in DeepSeek's training data ([source](https://trufflesecurity.com/blog/research-finds-12-000-live-api-keys-and-passwords-in-deepseek-s-training-data)). This is a real-world example of why opt-out matters.

### MANDATORY setup before using DeepSeek with any client data

1. Sign up at https://platform.deepseek.com
2. Top up $10-20 (~₹850-₹1700)
3. **Go to Settings → Privacy → toggle OFF "Improve the model for everyone"** — this is the opt-out
4. Settings → API Keys → Create New Key → copy the `sk-...` string immediately
5. **Verify the opt-out by reloading the page** — it must show OFF

### Connect to AI Brain India

Add to `~/.ailawfirm-india/config.json`:

```json
{
  "ai_provider": "anthropic-compatible",
  "base_url": "https://api.deepseek.com/anthropic",
  "api_key": "sk-YOUR-DEEPSEEK-KEY-HERE",
  "model": "deepseek-v4-pro"
}
```

### What's safe to use DeepSeek for (even with opt-out)

✅ Safe:
- Legal research summaries (you provide the source, DeepSeek summarizes)
- Drafting templates (general structure, no client facts)
- DPDP study sessions (learning the law, not applying it to a client)
- General writing assistance (your LinkedIn post, your blog)

❌ NOT safe (use Option A instead):
- Actual client matter drafts (names, facts, prayers)
- Confidential communications
- Strategy discussions involving real opposing parties
- Anything covered by attorney-client privilege

### Cost reality
- ~$0.50-2 per heavy day (~₹40-170/day for high-volume drafting)
- Light personal use: $0.10-0.30/day (~₹8-25/day)
- $10 lasts most users 4-8 weeks

---

## 🥉 Option C — Claude API (Anthropic)

### Why use it
- Top-tier quality (top-tier reasoning quality for complex research workflows)
- Anthropic's privacy posture is strong (they explicitly state API inputs are NOT used for training unless you opt in)
- Long context (1M tokens — can ingest full case files)

### Privacy fact
Per Anthropic's policy: **API customer data is NOT used to train models by default.** This is the inverse of DeepSeek — privacy is default-on. ([source](https://www.anthropic.com/legal/commercial-terms))

### Setup
1. Sign up at https://console.anthropic.com
2. Add billing · top up $20-50 (~₹1700-4200)
3. API Keys → Create → copy `sk-ant-...`

### Connect
```json
{
  "ai_provider": "anthropic",
  "api_key": "sk-ant-YOUR-KEY-HERE",
  "model": "claude-opus-4-7"
}
```

### Cost reality
- Heavy daily use: $30-150/month (~₹2500-12500/month)
- Light personal use: $5-20/month (~₹400-1700/month)

### When this makes sense
- You're billing >₹40,000/month and the tool is doing >5hr/week of real work for you
- You handle complex matters where the model's reasoning quality matters

---

## 🥉 Option D — Gemini API (Google)

### Why use it
- Largest context (1M tokens · Gemini 3.1 Pro)
- Cheaper than Claude
- Excellent for long-PDF reading + research synthesis

### Privacy fact
Per Google AI Studio terms: **paid API tier (Gemini API with billing) does NOT use prompts for training.** Free tier DOES. ([source](https://ai.google.dev/gemini-api/terms))

**Critical:** ensure you're on the PAID tier before using Gemini for any client data. The free tier opt-in to training is default.

### Setup
1. Sign up at https://aistudio.google.com
2. Set up billing (paid tier, not free)
3. Get API key

### Connect
```json
{
  "ai_provider": "google-gemini",
  "api_key": "AIza-YOUR-KEY-HERE",
  "model": "gemini-3.1-pro"
}
```

---

## 🎯 The right answer for most Indian solo advocates

**Use a hybrid:**
- **Local Ollama (Option A)** for everything involving actual client matter data
- **DeepSeek API with opt-out (Option B)** for drafting templates, study, generic writing
- Switch by editing one line in `~/.ailawfirm-india/config.json`

**Decision rule:** if the query mentions a real client name, real facts, or anything that could be construed as attorney-client privileged → use Ollama. Otherwise DeepSeek is fine.

---

## 🔒 Pro tip: rotate API keys quarterly

For any cloud API (DeepSeek · Claude · Gemini):
1. Create a new API key from the provider's dashboard
2. Replace the old one in `config.json`
3. Delete the old key from the provider's dashboard

Why: if your `config.json` ever leaks (laptop stolen, accidental git commit, etc.), the old key is dead. Standard infosec hygiene.

---

## 🆘 Troubleshooting

### "API key invalid"
- Double-check you copied the full key (including the `sk-` prefix for DeepSeek/Claude, `AIza` for Gemini)
- Confirm billing is active on the provider's dashboard
- Check the key wasn't deleted

### "Connection timed out"
- Cloud APIs need internet
- Check if your office firewall blocks the API URL (corporate networks often do)
- Try from your phone's hotspot to isolate

### "Model not found"
- Model names change. Check the provider's current model list:
  - DeepSeek: https://api-docs.deepseek.com
  - Anthropic: https://docs.anthropic.com/en/docs/models-overview
  - Gemini: https://ai.google.dev/gemini-api/docs/models

### Ollama is slow
- Use a smaller model: `ollama pull qwen3:7b`
- Close other apps to free up RAM
- On Mac, check Activity Monitor → Memory tab; if pressure is yellow/red, you need a smaller model

---

## Sources

- [DeepSeek Privacy Policy](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html) — official source for the opt-out toggle
- [DeepSeek 12K API key leak (Truffle Security)](https://trufflesecurity.com/blog/research-finds-12-000-live-api-keys-and-passwords-in-deepseek-s-training-data) — context for why opt-out matters
- [Anthropic Commercial Terms](https://www.anthropic.com/legal/commercial-terms) — API data not used for training by default
- [Google AI Studio Terms](https://ai.google.dev/gemini-api/terms) — paid vs free tier privacy difference

---

**Last verified:** 2026-05-18. AI provider terms change. Re-verify before relying on any privacy claim for client work.
---

## ⚠️ Third-party CLI tools and IDEs — user assumes all risk

If you integrate this Software with **any third-party AI service, CLI tool, or AI-assisted IDE** — including but not limited to: **Anthropic Claude API · Claude CLI · Claude Code · OpenAI API · Codex CLI · Google Gemini API · Gemini CLI · DeepSeek API · OpenCode · Cursor · GitHub Copilot · JetBrains AI · Mistral · Cohere · HuggingFace inference · Groq · Together AI · Qwen API · or any other model provider, CLI, IDE, or AI-assisted tool** — you do so **at your own risk** and under the terms of service of that third-party tool.

The publisher (Wolfgang_rush · Rushikesh R. Mahajan):

- Does **NOT** recommend any specific third-party tool
- Does **NOT** receive any compensation, referral fee, or benefit from any third-party tool's adoption
- Does **NOT** verify any third-party tool's privacy posture, security, or compliance with your jurisdiction's law
- Accepts **NO** responsibility for your choice of third-party tooling
- Accepts **NO** responsibility for any data leakage, confidentiality breach, professional-conduct violation, regulatory non-compliance, or any other harm resulting from your use of third-party tools alongside this Software
- Makes **NO** warranty that any third-party tool is suitable for legal-professional use in any jurisdiction

**You are solely responsible** for:

- Reading the privacy policy and terms of service of each third-party tool before connecting it
- Ensuring compliance with all confidentiality rules, data-protection laws, sectoral regulations, and bar conduct rules that apply to your practice
- Obtaining client consent where required before routing client data through any third-party tool
- Verifying that the third-party tool does not retain, train on, or share your queries in ways that breach your professional obligations
- Managing API keys, access tokens, and credentials securely (do not commit them to version control; use environment variables or a password manager)
- Independently verifying any output produced by a third-party tool before client-facing use

**This warning applies regardless of which third-party tool you choose, and regardless of any privacy claim that tool makes.** The responsibility to verify and the liability for use rest entirely with you.

---

