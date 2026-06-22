# 🙏 స్వాగతం, న్యాయవాది గారు — మీ AI Brain ఇక్కడ నుండి ప్రారంభమవుతుంది

> ⚠️ **ఈ అనువాదం AI-సహాయంతో తయారు చేయబడింది.** ఏదైనా పదం లేదా వాక్యం తప్పుగా అనిపిస్తే, దయచేసి [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) చూసి GitHub లో Pull Request పంపండి.

మీరు programmer అయి ఉండాల్సిన అవసరం లేదు. Mac కొనాల్సిన అవసరం లేదు. ఏ subscription అవసరం లేదు. మీకు కావలసినవి — ఒక Windows laptop లేదా Mac, internet (install కోసం మాత్రమే), మరియు 30 నిమిషాలు.

Copy-paste చేయగలిగితే, మీరు దీనిని నడపగలరు.

> **English:** [GETTING_STARTED.md](GETTING_STARTED.md) · **हिन्दी:** [GETTING_STARTED_HINDI.md](GETTING_STARTED_HINDI.md) · **मराठी:** [GETTING_STARTED_MARATHI.md](GETTING_STARTED_MARATHI.md)
> **Windows:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md) · **Mac:** [MAC_INSTALL.md](MAC_INSTALL.md) · **AI model:** [MODEL_SETUP.md](MODEL_SETUP.md)

---

## ✨ ఇది ఏమిటి, ఒక paragraph లో

ఒక ఉచిత tool — మీ laptop ను ఒక చిన్న ప్రైవేట్ చట్టపరమైన office assistant గా మారుస్తుంది. ఇది మీ అన్ని matters ను గుర్తుంచుకుంటుంది (ప్రతి case file, parties, hearings, orders, dates). ఇది భారతీయ legal citations ను parse చేస్తుంది (AIR · SCC · SCC OnLine). ఏ court కు ఏ jurisdiction అని చెబుతుంది. BCI Rule 36 risks ను flag చేస్తుంది. ఇది **మీ స్వంత computer పై** నడుస్తుంది — cloud లేదు, upload లేదు, మూడవ పక్షం మీ client data ను చదవలేదు. Open-source (MIT license).

## 💛 భారతీయ solo న్యాయవాదులకు ఎందుకు

- **తక్కువ మరచిపోతారు** — నెలల పాత matter context వెంటనే తిరిగి వస్తుంది.
- **తక్కువ deadlines miss అవుతాయి** — hearing dates, limitation periods track అవుతాయి.
- **BCI Rule 36 safe** — publishing కు ముందు firewall మీ language ను తనిఖీ చేస్తుంది.
- **డబ్బు ఆదా అవుతుంది** — Manupatra ₹15,000+/సంవత్సరం. ఇది ₹0.
- **Private గా ఉంటారు** — client matters laptop ను వదిలి వెళ్లవు.

## 🧠 లోపల 7 specialists నివసిస్తారు

| # | Specialist | ఏమి చేస్తారు |
|---|---|---|
| 🧠 | **Receptionist (మెదడు)** | మీరు చెప్పేది వింటాడు · సరైన specialist ను పిలుస్తాడు |
| 📂 | **Matter Manager** | ప్రతి active case file ను కలిగి ఉంటాడు |
| 📜 | **Citation Clerk** | AIR/SCC/SCC OnLine parse చేస్తాడు |
| 🏛️ | **Court Registrar** | court info · jurisdiction |
| ✍️ | **Drafting Assistant** | Wolfgang_rush plugins తో |
| 🛡️ | **Compliance Officer** | BCI Rule 36 + DPDP firewall |
| 📅 | **Deadline Tracker** | limitation + hearing dates |

మీరు Receptionist తో మాత్రమే మాట్లాడతారు. మిగతా వారు వెనుక పని చేస్తారు.

## 🚀 30 నిమిషాల్లో ప్రారంభించండి

### Step 1 — Python install
- **Mac:** [MAC_INSTALL.md](MAC_INSTALL.md) చూడండి
- **Windows:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md) చూడండి

### Step 2 — Tool install

Terminal (Mac) లేదా PowerShell (Windows) తెరిచి paste చేయండి:

```
pip install git+https://github.com/Wolfgangrush/ai-law-firm-india.git
```

### Step 3 — AI brain కనెక్షన్

| Choice | Cost | Privacy | ఎవరికి |
|---|---|---|---|
| 🥇 **Local (Ollama + Qwen3)** | ₹0 ఎప్పటికీ | 🟢 సంపూర్ణ | **client matters handle చేసే అందరికీ** |
| 🥈 **DeepSeek API** | ~₹80-200/నెల | ⚠️ మంచిది కానీ opt-out అవసరం | client కాని పని |
| 🥉 **Claude / Gemini API** | ~₹1500-5000/నెల | 🟢 బలమైనది | heavy daily users |

[MODEL_SETUP.md](MODEL_SETUP.md) చూడండి.

### Step 4 — మొదటి సంభాషణ

```
ailawfirm-india
```

వీటిని ప్రయత్నించండి:
```
> tell me about Telangana High Court
> validate AIR 1973 SC 1461
> check this language: "Best advocate in Hyderabad"
> what's the limitation period for a money suit?
```

## 🛡️ Privacy యొక్క నిజాయితీ వైపు

**Tool స్వయంగా:** అన్ని data మీ laptop లో `~/.ailawfirm-india/` folder లో. ఏ cloud కు upload లేదు.

**Cloud AI:** Cloud API ఉపయోగిస్తే, queries వారి servers కు వెళ్తాయి. నిజమైన client గోప్యత కోసం **local Ollama** ఉపయోగించండి.

## 📁 Data ఎక్కడ ఉంటుంది

```
~/.ailawfirm-india/                  ← Mac
C:\Users\YourName\.ailawfirm-india\  ← Windows
├── palace/                          ← మొత్తం memory
├── config.json                      ← settings
└── people_map.json                  ← optional aliases
```

Backup: ఈ folder USB / Dropbox / OneDrive కు copy చేయండి.

## 🙏 Credits

- **Engine:** a local memory architecture — అన్ని architectural credit వారికి.
- **Publisher:** [Wolfgang_rush](https://github.com/Wolfgangrush)
- **Author:** Rushikesh Mahajan, Advocate (your High Court Bench)

ఇది మీ వారం యొక్క ఒక గంటను ఆదా చేస్తే, tool తనను తాను వేయి సార్లు pay చేసుకుంది.

`మొదలుపెడదాం.` 🙏

---

**License:** MIT. **Disclaimer:** ఈ tool మీ practice ను organize చేయడానికి సహాయపడుతుంది. ఇది చట్టపరమైన సలహా ఇవ్వదు. BCI Rule 36 firewall built-in కానీ compliance బాధ్యత మీది.

**సరిచేయడానికి/మెరుగుపరచడానికి:** [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) చూడండి.
