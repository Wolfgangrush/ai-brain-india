# 🙏 ସ୍ୱାଗତ, ଓକିଲ ବାବୁ — ଆପଣଙ୍କର AI Brain ଏଠାରୁ ଆରମ୍ଭ

> ⚠️ **ଏହି ଅନୁବାଦ AI-ସହାୟତାରେ ପ୍ରସ୍ତୁତ କରାଯାଇଛି।** ଯଦି କୌଣସି ଶବ୍ଦ ବା ବାକ୍ୟ ଭୁଲ ଲାଗେ, ଦୟାକରି [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) ଦେଖନ୍ତୁ ଏବଂ GitHub ରେ Pull Request ପଠାନ୍ତୁ।

ଆପଣଙ୍କୁ programmer ହେବାର ଆବଶ୍ୟକତା ନାହିଁ। Mac କିଣିବାର ଆବଶ୍ୟକତା ନାହିଁ। କୌଣସି subscription ଆବଶ୍ୟକ ନୁହେଁ। ଆପଣଙ୍କୁ ଦରକାର — ଗୋଟିଏ Windows laptop କିମ୍ବା Mac, internet (କେବଳ install ପାଇଁ), ଏବଂ 30 ମିନିଟ୍।

ଯଦି ଆପଣ copy-paste କରିପାରନ୍ତି, ତେବେ ଆପଣ ଏହାକୁ ଚଲାଇ ପାରିବେ।

> **English:** [GETTING_STARTED.md](GETTING_STARTED.md) · **हिन्दी:** [GETTING_STARTED_HINDI.md](GETTING_STARTED_HINDI.md) · **मराठी:** [GETTING_STARTED_MARATHI.md](GETTING_STARTED_MARATHI.md)
> **Windows:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md) · **Mac:** [MAC_INSTALL.md](MAC_INSTALL.md) · **AI model:** [MODEL_SETUP.md](MODEL_SETUP.md)

---

## ✨ ଏହା କଣ, ଗୋଟିଏ paragraph ରେ

ଗୋଟିଏ ମାଗଣା tool ଯାହା ଆପଣଙ୍କ laptop କୁ ଗୋଟିଏ ଛୋଟ ବ୍ୟକ୍ତିଗତ ଆଇନ office assistant ରେ ପରିଣତ କରେ। ଏହା ଆପଣଙ୍କର ସମସ୍ତ matters ମନେ ରଖେ (ପ୍ରତ୍ୟେକ case file, parties, hearings, orders, dates)। ଏହା ଭାରତୀୟ legal citations parse କରେ (AIR · SCC · SCC OnLine)। କେଉଁ court ର କେଉଁଠାରେ jurisdiction ଅଛି କୁହେ। BCI Rule 36 risks flag କରେ। ଏହା **ଆପଣଙ୍କ ନିଜ computer ରେ** ଚାଲେ — cloud ନାହିଁ, upload ନାହିଁ, ତୃତୀୟ ପକ୍ଷ ଆପଣଙ୍କ client data ପଢ଼ିପାରିବେ ନାହିଁ। Open-source (MIT license)।

## 💛 ଭାରତର solo ଓକିଲମାନଙ୍କ ପାଇଁ କାହିଁକି

- **କମ୍ ଭୁଲିବେ** — ମାସର ପୁରୁଣା matter ର context ତୁରନ୍ତ ଫେରିଆସେ।
- **କମ୍ deadlines miss ହେବ** — hearing dates ଏବଂ limitation periods track ହୁଏ।
- **BCI Rule 36 safe** — publishing ପୂର୍ବରୁ firewall ଆପଣଙ୍କ language ଯାଞ୍ଚ କରେ।
- **ଟଙ୍କା ସଞ୍ଚୟ ହେବ** — Manupatra ₹15,000+/ବର୍ଷ। ଏହା ₹0।
- **Private ରହିବେ** — client matters laptop ରୁ ବାହାରେ ଯାଆନ୍ତି ନାହିଁ।

## 🧠 ଭିତରେ 7 specialists ରୁହନ୍ତି

| # | Specialist | କଣ କରନ୍ତି |
|---|---|---|
| 🧠 | **Receptionist (ମସ୍ତିଷ୍କ)** | ଆପଣ ଯାହା କୁହନ୍ତି ଶୁଣେ · ସଠିକ୍ specialist କୁ ଡାକେ |
| 📂 | **Matter Manager** | ପ୍ରତ୍ୟେକ active case file ରଖେ |
| 📜 | **Citation Clerk** | AIR/SCC/SCC OnLine parse କରେ |
| 🏛️ | **Court Registrar** | court info · jurisdiction |
| ✍️ | **Drafting Assistant** | Wolfgang_rush plugins ସହ |
| 🛡️ | **Compliance Officer** | BCI Rule 36 + DPDP firewall |
| 📅 | **Deadline Tracker** | limitation + hearing dates |

ଆପଣ କେବଳ Receptionist ସହ କଥା କୁହନ୍ତି। ବାକି backstage ରେ କାମ କରନ୍ତି।

## 🚀 30 ମିନିଟ୍ ରେ ଆରମ୍ଭ

### Step 1 — Python install
- **Mac:** [MAC_INSTALL.md](MAC_INSTALL.md) ଦେଖନ୍ତୁ
- **Windows:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md) ଦେଖନ୍ତୁ

### Step 2 — Tool install

Terminal (Mac) କିମ୍ବା PowerShell (Windows) ଖୋଲି paste କରନ୍ତୁ:

```
pip install git+https://github.com/Wolfgangrush/ai-law-firm-india.git
```

### Step 3 — AI brain ସଂଯୋଗ

| Choice | Cost | Privacy | କାହାପାଇଁ |
|---|---|---|---|
| 🥇 **Local (Ollama + Qwen3)** | ₹0 ସର୍ବଦା | 🟢 ସମ୍ପୂର୍ଣ୍ଣ | **client matters handle କରୁଥିବା ସମସ୍ତଙ୍କ ପାଇଁ** |
| 🥈 **DeepSeek API** | ~₹80-200/ମାସ | ⚠️ ଭଲ କିନ୍ତୁ opt-out ଦରକାର | client ନୁହେଁ କାମ |
| 🥉 **Claude / Gemini API** | ~₹1500-5000/ମାସ | 🟢 ଶକ୍ତିଶାଳୀ | heavy daily users |

[MODEL_SETUP.md](MODEL_SETUP.md) ଦେଖନ୍ତୁ।

### Step 4 — ପ୍ରଥମ କଥୋପକଥନ

```
ailawfirm-india
```

ଏଗୁଡ଼ିକ try କରନ୍ତୁ:
```
> tell me about Orissa High Court
> validate AIR 1973 SC 1461
> check this language: "Best advocate in Bhubaneswar"
> what's the limitation period for a money suit?
```

## 🛡️ Privacy ର ସତ୍ୟ ପକ୍ଷ

**Tool ନିଜେ:** ସମସ୍ତ data ଆପଣଙ୍କ laptop ରେ `~/.ailawfirm-india/` folder ରେ। କୌଣସି cloud ରେ upload ନୁହେଁ।

**Cloud AI:** Cloud API ବ୍ୟବହାର କଲେ queries ସେମାନଙ୍କ servers କୁ ଯାଏ। ପ୍ରକୃତ client ଗୋପନୀୟତା ପାଇଁ **local Ollama** ବ୍ୟବହାର କରନ୍ତୁ।

## 📁 Data କେଉଁଠାରେ ରୁହେ

```
~/.ailawfirm-india/                  ← Mac
C:\Users\YourName\.ailawfirm-india\  ← Windows
├── palace/                          ← ସମସ୍ତ memory
├── config.json                      ← settings
└── people_map.json                  ← optional aliases
```

Backup: ଏହି folder USB / Dropbox / OneDrive କୁ copy କରନ୍ତୁ।

## 🙏 Credits

- **Engine:** a local memory architecture — ସମସ୍ତ architectural credit ସେମାନଙ୍କୁ।
- **Publisher:** [Wolfgang_rush](https://github.com/Wolfgangrush)
- **Author:** Rushikesh Mahajan, Advocate (your High Court Bench)

ଯଦି ଏହା ଆପଣଙ୍କ ସପ୍ତାହର ଗୋଟିଏ ଘଣ୍ଟା ସଞ୍ଚୟ କରେ, tool ନିଜକୁ ହଜାର ଥର pay କରିଛି।

`ଆରମ୍ଭ କରିବା।` 🙏

---

**License:** MIT। **Disclaimer:** ଏହି tool ଆପଣଙ୍କ practice organize କରିବାରେ ସାହାଯ୍ୟ କରେ। ଏହା ଆଇନଗତ ପରାମର୍ଶ ଦିଏ ନାହିଁ। BCI Rule 36 firewall built-in ଅଛି କିନ୍ତୁ compliance ର ଦାୟିତ୍ୱ ଆପଣଙ୍କର।

**ସୁଧାର ପାଇଁ:** [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) ଦେଖନ୍ତୁ।
