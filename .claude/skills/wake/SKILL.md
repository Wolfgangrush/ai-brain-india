---
name: wake
description: Start-of-session state loader for India AI Brain users. Runs 2-pass leak-check (Rule 1: same scope as retrospective — no internal-shorthand, no internal-paths, no personal-build references). Loads jurisdiction context so every session begins informed.
allowed-tools: Bash, Read, Glob
---

# /wake — Start-of-Session State Loader (India)

Loads the India AI Brain's current state at session start. Displays readiness so the user knows exactly what's available before they begin work.

## 2-Pass Leak-Check (Rule 1 — execute FIRST, before displaying state)

### Pass 1 — Internal-shorthand codes + internal paths
```bash
# Detect any 2-5 letter all-caps token (potential internal matter shorthand)
grep -rniE '\b[A-Z]{2,5}\b' --include="*.md" --include="*.json" --include="*.txt" . 2>/dev/null \
  | grep -vE '\b(USA|UK|EU|UAE|HC|SC|API|JSON|MIT|MCP|CSV|PDF|XML|HTML|HTTP|URL|ABN|TFN|GST|VAT|CEO|CFO|CIO|MD|QC|SC|JD|LLM|LLB|BSc|MBA|GDP|GDPR|CCPA|DPDP|AI|ML|NLP|CLI|IDE|SDK|README|CI|CD|PR|RFC|ETA|EOD|TBD|FYI|NB|AM|PM)\b'
# Detect references to user-home dot-directories (potential machine-internal paths)
grep -rniE '~/\.[a-z]+/' --include="*.md" --include="*.json" . 2>/dev/null
```
**Expected: zero hits.** Any hit = flag immediately. Do not proceed silently.

### Pass 2 — External architecture references + personal-vs-business markers
```bash
# Detect references to external project-architecture names (extend this regex with your firm's internal terms)
grep -rniE 'YOUR_INTERNAL_ARCHITECTURE_PATTERN_HERE' --include="*.md" --include="*.json" . 2>/dev/null
# Detect personal-build references (extend with your firm's specific personal-vs-business markers if any)
grep -rniE 'YOUR_PERSONAL_VS_BUSINESS_MARKER_HERE' --include="*.md" --include="*.json" . 2>/dev/null
```
**Expected: zero hits.** Any hit = flag immediately.

## Workflow

### Step 1: Run 2-pass leak-check (above)
If either pass fails, display warning before proceeding.

### Step 2: System state check
```bash
echo "Python: $(python3 --version 2>&1)"
echo "Package: $(pip show ailawfirm_india 2>&1 | head -3)"
echo "Data dir: $(ls -la ~/.ailawfirm-india/ 2>&1 | head -5)"
echo "Config: $(cat ~/.ailawfirm-india/config.json 2>&1 | head -10)"

# v0.1.2 thermal hygiene state (helpful on fanless 8GB Macs)
echo ""
echo "Thermal hygiene (v0.1.2):"
if [ -f ~/.ailawfirm-india/lite.flag ] || [ "$AILAWFIRM_LITE" = "1" ]; then
  echo "  Lite mode: ON — drafts save as .md · run 'ailawfirm-india finalize <matter>' at session end for .docx"
else
  echo "  Lite mode: OFF (default)"
  echo "  → If your Mac runs hot during long sessions:  ailawfirm-india lite on"
fi
echo "  → Diagnose anytime:                            ailawfirm-india doctor"
echo "  → Batch-generate .docx for a matter folder:    ailawfirm-india finalize <matter>"
```

### Step 3: Jurisdiction context
Display the India-specific legal framework:
- **Supreme Court of India** + **23 High Courts** (Allahabad · Bombay · Calcutta · Delhi · Gauhati · Gujarat · Himachal Pradesh · Jammu & Kashmir · Jharkhand · Karnataka · Kerala · Madhya Pradesh · Madras · Manipur · Meghalaya · Orissa · Patna · Punjab & Haryana · Rajasthan · Sikkim · Tripura · Uttarakhand · Chhattisgarh · Telangana · Andhra Pradesh)
- **Statutes:** CPC 1908 · CrPC 1973 / BNSS 2023 · IPC 1860 / BNS 2023 · Evidence Act 1872 / BSA 2023 · Constitution of India · Limitation Act 1963 · DPDP Act 2023 · IT Act 2000 · Contract Act 1872
- **BCI Rules:** Rule 36 (solicitation/advertising firewall) ACTIVE

### Step 4: Specialists available
| # | Specialist | Status |
|---|---|---|
| 🧠 | Receptionist (brain) | READY |
| 📂 | Matter Manager | READY |
| 📜 | Citation Clerk | READY |
| 🏛️ | Court Registrar | READY |
| ✍️ | Drafting Assistant | READY |
| 🛡️ | Compliance Officer | READY |
| 📅 | Deadline Tracker | READY |

### Step 5: Present readiness summary

## Output Format

```markdown
## 🇮🇳 India AI Brain — Ready

🟢 Leak-check: PASS (Pass 1 clean · Pass 2 clean)

**System:**
- Python: [version]
- Package: ailawfirm_india [version]
- Data: ~/.ailawfirm-india/ [status]

**7 specialists online.**
**14 High Courts + Supreme Court mapped.**
**DPDP Act 2023 · BNS 2023 · BSA 2023 mapped as jurisdiction context** (full statute text arrives in v0.2).

🧠 This firm LEARNS. Every session makes the next one smarter.
   Run `/retrospective` at session end to save what you learned.

---
What do you need today?
```

## Anti-Pollution Rules (DO NOT BREAK)
- Never reference user-home dot-directories or absolute paths from a developer's machine
- Never use internal entity codes
- Never reference external project-architecture names not tied to this firm
- Never reference the publisher's personal builds or personal-vs-business markers

## What this skill does NOT do
- Does NOT read or write to the local memory layer
- Does NOT access personal diary or KG
- Does NOT touch any other firm's directory
- Does NOT modify any file (read-only state display)
