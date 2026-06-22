# 🙏 સ્વાગત છે, વકીલ સાહેબ — તમારી AI Brain અહીંથી શરૂ થાય છે

> ⚠️ **આ અનુવાદ AI-સહાયથી તૈયાર કરવામાં આવ્યો છે.** કોઈ શબ્દ કે વાક્ય ખોટું લાગે, તો કૃપા કરીને [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) જુઓ અને GitHub પર Pull Request મોકલો.

તમારે programmer હોવાની જરૂર નથી. Mac ખરીદવાની જરૂર નથી. કોઈ subscription જરૂરી નથી. તમારે જોઈએ — એક Windows laptop કે Mac, internet (ફક્ત install માટે), અને 30 મિનિટ.

જો તમે copy-paste કરી શકો, તો તમે આ ચલાવી શકો છો.

> **English:** [GETTING_STARTED.md](GETTING_STARTED.md) · **हिन्दी:** [GETTING_STARTED_HINDI.md](GETTING_STARTED_HINDI.md) · **मराठी:** [GETTING_STARTED_MARATHI.md](GETTING_STARTED_MARATHI.md)
> **Windows:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md) · **Mac:** [MAC_INSTALL.md](MAC_INSTALL.md) · **AI model:** [MODEL_SETUP.md](MODEL_SETUP.md)

---

## ✨ આ શું છે, એક paragraph માં

એક મફત tool જે તમારા laptop ને એક નાનું ખાનગી કાનૂની office assistant બનાવે છે. તે તમારી બધી matters યાદ રાખે છે (દરેક case file, parties, hearings, orders, dates). તે ભારતીય legal citations parse કરે છે (AIR · SCC · SCC OnLine). કયા court ની કયાં jurisdiction છે તે કહે છે. BCI Rule 36 risks flag કરે છે. તે **તમારા પોતાના computer પર** ચાલે છે — cloud નથી, upload નથી, ત્રીજો પક્ષ તમારા client data વાંચી શકતો નથી. Open-source (MIT license).

## 💛 ભારતના solo વકીલો માટે કેમ

- **ઓછું ભૂલશો** — મહિનાઓ જૂના matter નો context તરત પાછો આવે.
- **ઓછી deadlines miss થશે** — hearing dates અને limitation periods track થાય.
- **BCI Rule 36 safe** — publishing પહેલા firewall તમારી language ચકાસે.
- **પૈસા બચશે** — Manupatra ₹15,000+/વર્ષ. આ ₹0.
- **Private રહેશો** — client matters laptop માંથી નીકળતા નથી.

## 🧠 અંદર 7 specialists રહે છે

| # | Specialist | શું કરે |
|---|---|---|
| 🧠 | **Receptionist (મગજ)** | તમે જે કહો તે સાંભળે · સાચા specialist ને બોલાવે |
| 📂 | **Matter Manager** | દરેક active case file રાખે |
| 📜 | **Citation Clerk** | AIR/SCC/SCC OnLine parse કરે |
| 🏛️ | **Court Registrar** | court info · jurisdiction |
| ✍️ | **Drafting Assistant** | Wolfgang_rush plugins સાથે |
| 🛡️ | **Compliance Officer** | BCI Rule 36 + DPDP firewall |
| 📅 | **Deadline Tracker** | limitation + hearing dates |

તમે ફક્ત Receptionist સાથે વાત કરો. બાકીના પાછળ કામ કરે.

## 🚀 30 મિનિટમાં શરૂઆત

### Step 1 — Python install
- **Mac:** [MAC_INSTALL.md](MAC_INSTALL.md) જુઓ
- **Windows:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md) જુઓ

### Step 2 — Tool install

Terminal (Mac) અથવા PowerShell (Windows) ખોલીને paste કરો:

```
pip install git+https://github.com/Wolfgangrush/ai-law-firm-india.git
```

### Step 3 — AI brain જોડાણ

| Choice | Cost | Privacy | કોના માટે |
|---|---|---|---|
| 🥇 **Local (Ollama + Qwen3)** | ₹0 કાયમ માટે | 🟢 સંપૂર્ણ | **client matters handle કરનાર બધા માટે** |
| 🥈 **DeepSeek API** | ~₹80-200/મહિનો | ⚠️ સારી પણ opt-out જરૂરી | client નહીં એવું કામ |
| 🥉 **Claude / Gemini API** | ~₹1500-5000/મહિનો | 🟢 મજબૂત | heavy daily users |

[MODEL_SETUP.md](MODEL_SETUP.md) જુઓ.

### Step 4 — પ્રથમ વાતચીત

```
ailawfirm-india
```

આ try કરો:
```
> tell me about Gujarat High Court
> validate AIR 1973 SC 1461
> check this language: "Best advocate in Ahmedabad"
> what's the limitation period for a money suit?
```

## 🛡️ Privacy ની પ્રામાણિક બાજુ

**Tool પોતે:** બધો data તમારા laptop પર `~/.ailawfirm-india/` folder માં. કોઈ cloud પર upload નથી.

**Cloud AI:** Cloud API વાપરો તો queries તેમના servers પર જાય. ખરી client ગુપ્તતા માટે **local Ollama** વાપરો.

## 📁 Data ક્યાં રહે

```
~/.ailawfirm-india/                  ← Mac
C:\Users\YourName\.ailawfirm-india\  ← Windows
├── palace/                          ← બધી memory
├── config.json                      ← settings
└── people_map.json                  ← optional aliases
```

Backup: આ folder USB / Dropbox / OneDrive પર copy કરો.

## 🙏 Credits

- **Engine:** a local memory architecture — બધો architectural credit તેમને.
- **Publisher:** [Wolfgang_rush](https://github.com/Wolfgangrush)
- **Author:** Rushikesh Mahajan, Advocate (your High Court Bench)

જો આ તમારા અઠવાડિયાનો એક કલાક બચાવે, tool એ પોતાને હજાર વાર pay કરી દીધો.

`ચાલો શરૂ કરીએ.` 🙏

---

**License:** MIT. **Disclaimer:** આ tool તમારી practice organize કરવામાં મદદ કરે. તે કાનૂની સલાહ આપતું નથી. BCI Rule 36 firewall built-in છે પણ compliance ની જવાબદારી તમારી છે.

**સુધારા/વધારા માટે:** [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) જુઓ.
