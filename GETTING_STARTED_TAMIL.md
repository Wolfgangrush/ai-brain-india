# 🙏 வரவேற்கிறேன், வழக்கறிஞரே — உங்கள் AI Brain இங்கிருந்து தொடங்குகிறது

> ⚠️ **இந்த மொழிபெயர்ப்பு AI-உதவியுடன் தயாரிக்கப்பட்டது.** ஏதேனும் சொல் அல்லது வாக்கியம் தவறாக இருந்தால், தயவுசெய்து [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) பார்த்து GitHub-இல் Pull Request அனுப்புங்கள்.

நீங்கள் programmer ஆக இருக்க வேண்டிய அவசியமில்லை. Mac வாங்க வேண்டிய அவசியமில்லை. எந்த subscription-ம் தேவையில்லை. உங்களுக்கு வேண்டியது — ஒரு Windows laptop அல்லது Mac, internet (install-க்கு மட்டும்), மற்றும் 30 நிமிடங்கள்.

Copy-paste செய்ய முடிந்தால், நீங்கள் இதை இயக்க முடியும்.

> **English:** [GETTING_STARTED.md](GETTING_STARTED.md) · **हिन्दी:** [GETTING_STARTED_HINDI.md](GETTING_STARTED_HINDI.md) · **मराठी:** [GETTING_STARTED_MARATHI.md](GETTING_STARTED_MARATHI.md)
> **Windows:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md) · **Mac:** [MAC_INSTALL.md](MAC_INSTALL.md) · **AI model:** [MODEL_SETUP.md](MODEL_SETUP.md)

---

## ✨ இது என்ன, ஒரு பத்தியில்

ஒரு இலவச tool — உங்கள் laptop-ஐ ஒரு சிறிய தனிப்பட்ட சட்ட அலுவலக assistant ஆக மாற்றுகிறது. இது உங்கள் அனைத்து matters-ஐயும் நினைவில் வைக்கிறது (ஒவ்வொரு case file, parties, hearings, orders, dates). இது இந்திய legal citations-ஐ parse செய்கிறது (AIR · SCC · SCC OnLine). எந்த court-க்கு என்ன jurisdiction என்று சொல்கிறது. BCI Rule 36 risks-ஐ flag செய்கிறது. இது **உங்கள் சொந்த computer-இல்** இயங்குகிறது — cloud இல்லை, upload இல்லை, மூன்றாம் தரப்பினர் உங்கள் client data-ஐ படிக்க முடியாது. Open-source (MIT license).

## 💛 இந்திய solo வழக்கறிஞர்களுக்கு ஏன்

- **குறைவாக மறப்பீர்கள்** — மாதங்கள் பழைய matter context உடனே திரும்பும்.
- **குறைவான deadlines miss ஆகும்** — hearing dates, limitation periods track ஆகும்.
- **BCI Rule 36 safe** — publishing-க்கு முன் firewall உங்கள் language-ஐ சரிபார்க்கிறது.
- **பணம் சேமிக்கப்படும்** — Manupatra ₹15,000+/வருடம். இது ₹0.
- **Private-ஆக இருப்பீர்கள்** — client matters laptop-ஐ விட்டு வெளியேறுவதில்லை.

## 🧠 உள்ளே 7 specialists வசிக்கிறார்கள்

| # | Specialist | என்ன செய்கிறார்கள் |
|---|---|---|
| 🧠 | **Receptionist (மூளை)** | நீங்கள் கேட்பதை கேட்கிறார் · சரியான specialist-ஐ அழைக்கிறார் |
| 📂 | **Matter Manager** | ஒவ்வொரு active case file-ஐயும் வைத்திருக்கிறார் |
| 📜 | **Citation Clerk** | AIR/SCC/SCC OnLine parse செய்கிறார் |
| 🏛️ | **Court Registrar** | court-தகவல்கள் · jurisdiction |
| ✍️ | **Drafting Assistant** | Wolfgang_rush plugins-உடன் |
| 🛡️ | **Compliance Officer** | BCI Rule 36 + DPDP firewall |
| 📅 | **Deadline Tracker** | limitation + hearing dates |

நீங்கள் Receptionist-உடன் மட்டுமே பேசுகிறீர்கள். மற்றவர்கள் backstage-இல் வேலை செய்கிறார்கள்.

## 🚀 30 நிமிடங்களில் தொடங்குங்கள்

### Step 1 — Python install
- **Mac:** [MAC_INSTALL.md](MAC_INSTALL.md) பார்க்கவும்
- **Windows:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md) பார்க்கவும்

### Step 2 — Tool install

Terminal (Mac) அல்லது PowerShell (Windows) திறந்து paste செய்யுங்கள்:

```
pip install git+https://github.com/Wolfgangrush/ai-law-firm-india.git
```

### Step 3 — AI brain இணைப்பு

| Choice | Cost | Privacy | யாருக்கு |
|---|---|---|---|
| 🥇 **Local (Ollama + Qwen3)** | ₹0 எப்போதும் | 🟢 சரியான | **client matters handle செய்பவர்கள் அனைவருக்கும்** |
| 🥈 **DeepSeek API** | ~₹80-200/மாதம் | ⚠️ நல்லது ஆனால் opt-out தேவை | client-அல்லாத வேலை |
| 🥉 **Claude / Gemini API** | ~₹1500-5000/மாதம் | 🟢 வலுவான | heavy daily users |

[MODEL_SETUP.md](MODEL_SETUP.md) பார்க்கவும்.

### Step 4 — முதல் உரையாடல்

```
ailawfirm-india
```

இவற்றை முயற்சிக்கவும்:
```
> tell me about Madras High Court
> validate AIR 1973 SC 1461
> check this language: "Best advocate in Chennai"
> what's the limitation period for a money suit?
```

## 🛡️ Privacy-இன் நேர்மையான பக்கம்

**Tool தானே:** அனைத்து data உங்கள் laptop-இல் `~/.ailawfirm-india/` folder-இல். எந்த cloud-இலும் upload இல்லை.

**Cloud AI:** Cloud API பயன்படுத்தினால், queries அவர்களின் servers-க்கு செல்லும். உண்மையான client confidentiality-க்கு **local Ollama** பயன்படுத்துங்கள்.

## 📁 Data எங்கே இருக்கிறது

```
~/.ailawfirm-india/                  ← Mac
C:\Users\YourName\.ailawfirm-india\  ← Windows
├── palace/                          ← அனைத்து memory
├── config.json                      ← settings
└── people_map.json                  ← optional aliases
```

Backup: இந்த folder USB / Dropbox / OneDrive-க்கு copy செய்யுங்கள்.

## 🙏 Credits

- **Engine:** a local memory architecture — அனைத்து architectural credit அவர்களுக்கு.
- **Publisher:** [Wolfgang_rush](https://github.com/Wolfgangrush)
- **Author:** Rushikesh Mahajan, Advocate (your High Court Bench)

இது உங்கள் வாரத்தின் ஒரு மணி நேரத்தை சேமித்தால், tool தன்னை ஆயிரம் முறை pay செய்துவிட்டது.

`ஆரம்பிக்கலாம்.` 🙏

---

**License:** MIT. **Disclaimer:** இந்த tool உங்கள் practice-ஐ organize செய்ய உதவுகிறது. இது சட்ட ஆலோசனை வழங்காது. BCI Rule 36 firewall built-in ஆனால் compliance பொறுப்பு உங்களுடையது.

**சரிசெய்தல்/மேம்பாட்டிற்கு:** [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) பார்க்கவும்.
