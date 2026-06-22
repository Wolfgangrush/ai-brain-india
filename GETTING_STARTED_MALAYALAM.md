# 🙏 സ്വാഗതം, അഭിഭാഷകരേ — നിങ്ങളുടെ AI Brain ഇവിടെ നിന്ന് ആരംഭിക്കുന്നു

> ⚠️ **ഈ പരിഭാഷ AI-സഹായത്തോടെ തയ്യാറാക്കിയതാണ്.** ഏതെങ്കിലും വാക്കോ വാക്യമോ തെറ്റാണെന്ന് തോന്നിയാൽ, ദയവായി [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) കാണുകയും GitHub-ൽ Pull Request അയക്കുകയും ചെയ്യുക.

നിങ്ങൾ programmer ആകേണ്ടതില്ല. Mac വാങ്ങേണ്ടതില്ല. ഒരു subscription വേണ്ടതില്ല. നിങ്ങൾക്ക് വേണ്ടത് — ഒരു Windows laptop അല്ലെങ്കിൽ Mac, internet (install-ന് മാത്രം), 30 മിനിറ്റ്.

Copy-paste ചെയ്യാൻ കഴിയുമെങ്കിൽ, നിങ്ങൾക്ക് ഇത് പ്രവർത്തിപ്പിക്കാം.

> **English:** [GETTING_STARTED.md](GETTING_STARTED.md) · **हिन्दी:** [GETTING_STARTED_HINDI.md](GETTING_STARTED_HINDI.md) · **मराठी:** [GETTING_STARTED_MARATHI.md](GETTING_STARTED_MARATHI.md)
> **Windows:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md) · **Mac:** [MAC_INSTALL.md](MAC_INSTALL.md) · **AI model:** [MODEL_SETUP.md](MODEL_SETUP.md)

---

## ✨ ഇത് എന്താണ്, ഒരു paragraph-ൽ

ഒരു സൗജന്യ tool — നിങ്ങളുടെ laptop-നെ ഒരു ചെറിയ സ്വകാര്യ നിയമ office assistant ആക്കി മാറ്റുന്നു. ഇത് നിങ്ങളുടെ എല്ലാ matters-ഉം ഓർമ്മിക്കുന്നു (ഓരോ case file, parties, hearings, orders, dates). ഇത് ഇന്ത്യൻ legal citations parse ചെയ്യുന്നു (AIR · SCC · SCC OnLine). ഏത് court-ന് ഏത് jurisdiction എന്ന് പറയുന്നു. BCI Rule 36 risks flag ചെയ്യുന്നു. ഇത് **നിങ്ങളുടെ സ്വന്തം computer-ൽ** പ്രവർത്തിക്കുന്നു — cloud ഇല്ല, upload ഇല്ല, മൂന്നാം കക്ഷിക്ക് നിങ്ങളുടെ client data വായിക്കാൻ കഴിയില്ല. Open-source (MIT license).

## 💛 ഇന്ത്യൻ solo അഭിഭാഷകർക്ക് എന്തുകൊണ്ട്

- **കുറവ് മറക്കും** — മാസങ്ങൾ പഴയ matter context ഉടനെ തിരികെ വരും.
- **കുറവ് deadlines miss ആകും** — hearing dates, limitation periods track ആകും.
- **BCI Rule 36 safe** — publishing-ന് മുൻപ് firewall നിങ്ങളുടെ language പരിശോധിക്കും.
- **പണം ലാഭിക്കും** — Manupatra ₹15,000+/വർഷം. ഇത് ₹0.
- **Private-ആയിരിക്കും** — client matters laptop-ൽ നിന്ന് പുറത്തുപോകില്ല.

## 🧠 അകത്ത് 7 specialists ഉണ്ട്

| # | Specialist | എന്ത് ചെയ്യുന്നു |
|---|---|---|
| 🧠 | **Receptionist (തലച്ചോറ്)** | നിങ്ങൾ പറയുന്നത് കേൾക്കുന്നു · ശരിയായ specialist-നെ വിളിക്കുന്നു |
| 📂 | **Matter Manager** | ഓരോ active case file സൂക്ഷിക്കുന്നു |
| 📜 | **Citation Clerk** | AIR/SCC/SCC OnLine parse ചെയ്യുന്നു |
| 🏛️ | **Court Registrar** | court info · jurisdiction |
| ✍️ | **Drafting Assistant** | Wolfgang_rush plugins-മായി |
| 🛡️ | **Compliance Officer** | BCI Rule 36 + DPDP firewall |
| 📅 | **Deadline Tracker** | limitation + hearing dates |

നിങ്ങൾ Receptionist-മായി മാത്രമേ സംസാരിക്കുകയുള്ളൂ. ബാക്കിയുള്ളവർ backstage-ൽ പ്രവർത്തിക്കുന്നു.

## 🚀 30 മിനിറ്റിൽ ആരംഭിക്കുക

### Step 1 — Python install
- **Mac:** [MAC_INSTALL.md](MAC_INSTALL.md) കാണുക
- **Windows:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md) കാണുക

### Step 2 — Tool install

Terminal (Mac) അല്ലെങ്കിൽ PowerShell (Windows) തുറന്ന് paste ചെയ്യുക:

```
pip install git+https://github.com/Wolfgangrush/ai-law-firm-india.git
```

### Step 3 — AI brain കണക്ഷൻ

| Choice | Cost | Privacy | ആർക്ക് |
|---|---|---|---|
| 🥇 **Local (Ollama + Qwen3)** | ₹0 എന്നേക്കും | 🟢 പൂർണ്ണം | **client matters handle ചെയ്യുന്നവർക്കെല്ലാം** |
| 🥈 **DeepSeek API** | ~₹80-200/മാസം | ⚠️ നല്ലത് പക്ഷേ opt-out വേണം | client അല്ലാത്ത ജോലി |
| 🥉 **Claude / Gemini API** | ~₹1500-5000/മാസം | 🟢 ശക്തമായത് | heavy daily users |

[MODEL_SETUP.md](MODEL_SETUP.md) കാണുക.

### Step 4 — ആദ്യ സംഭാഷണം

```
ailawfirm-india
```

ഇവ try ചെയ്യുക:
```
> tell me about Kerala High Court
> validate AIR 1973 SC 1461
> check this language: "Best advocate in Kochi"
> what's the limitation period for a money suit?
```

## 🛡️ Privacy-യുടെ സത്യസന്ധമായ ഭാഗം

**Tool സ്വയം:** എല്ലാ data നിങ്ങളുടെ laptop-ൽ `~/.ailawfirm-india/` folder-ൽ. ഏതെങ്കിലും cloud-ൽ upload ഇല്ല.

**Cloud AI:** Cloud API ഉപയോഗിച്ചാൽ queries അവരുടെ servers-ൽ പോകും. യഥാർത്ഥ client രഹസ്യാത്മകതയ്ക്ക് **local Ollama** ഉപയോഗിക്കുക.

## 📁 Data എവിടെ താമസിക്കുന്നു

```
~/.ailawfirm-india/                  ← Mac
C:\Users\YourName\.ailawfirm-india\  ← Windows
├── palace/                          ← എല്ലാ memory
├── config.json                      ← settings
└── people_map.json                  ← optional aliases
```

Backup: ഈ folder USB / Dropbox / OneDrive-ലേക്ക് copy ചെയ്യുക.

## 🙏 Credits

- **Engine:** a local memory architecture — എല്ലാ architectural credit അവർക്ക്.
- **Publisher:** [Wolfgang_rush](https://github.com/Wolfgangrush)
- **Author:** Rushikesh Mahajan, Advocate (your High Court Bench)

ഇത് നിങ്ങളുടെ ആഴ്ചയിലെ ഒരു മണിക്കൂർ ലാഭിച്ചാൽ, tool സ്വയം ആയിരം തവണ pay ചെയ്തു.

`തുടങ്ങാം.` 🙏

---

**License:** MIT. **Disclaimer:** ഈ tool നിങ്ങളുടെ practice organize ചെയ്യാൻ സഹായിക്കുന്നു. ഇത് നിയമോപദേശം നൽകുന്നില്ല. BCI Rule 36 firewall built-in പക്ഷേ compliance-ന്റെ ഉത്തരവാദിത്തം നിങ്ങളുടേതാണ്.

**തിരുത്തലുകൾക്ക്:** [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) കാണുക.
