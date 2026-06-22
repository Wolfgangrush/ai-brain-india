# 🙏 स्वागत आहे, वकील साहेब — तुमची AI Brain इथून सुरू

तुम्हाला programmer असण्याची गरज नाही. Mac विकत घेण्याची गरज नाही. कोणत्याही subscription ची गरज नाही. तुम्हाला हवं — एक Windows laptop किंवा Mac, internet (फक्त install साठी), आणि 30 मिनिटं.

जर तुम्ही copy-paste करू शकत असाल, तर तुम्ही हे चालवू शकता.

> **English:** [GETTING_STARTED.md](GETTING_STARTED.md)
> **Hindi (हिन्दी):** [GETTING_STARTED_HINDI.md](GETTING_STARTED_HINDI.md)
> **Windows install:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md)
> **Mac install:** [MAC_INSTALL.md](MAC_INSTALL.md)
> **AI model कसा जोडायचा:** [MODEL_SETUP.md](MODEL_SETUP.md)

---

## ✨ हे काय आहे, एका paragraph मध्ये

एक मोफत tool जे तुमच्या laptop चं एक छोटं खाजगी कायदेशीर office assistant बनवतं. हे तुमचे सर्व मॅटर्स लक्षात ठेवतं (प्रत्येक case file, प्रत्येक party, प्रत्येक order, प्रत्येक hearing ची तारीख). हे भारतीय legal citations parse करतं (AIR · SCC · SCC OnLine). हे सांगतं कोणत्या court ची jurisdiction कुठे आहे. हे BCI Rule 36 चे risks flag करतं. हे **तुमच्या स्वतःच्या computer वर** चालतं — cloud नाही, upload नाही, तिसरा कोणी तुमच्या client चा data वाचत नाही. हे open-source आहे (MIT license).

## 💛 भारतातील solo वकिलाला हे का हवं

- **तुम्ही कमी विसराल.** महिन्यांपूर्वीच्या मॅटरचा context लगेच परत येईल.
- **Deadlines कमी चुकतील.** Hearing dates आणि limitation periods track होतात.
- **BCI Rule 36 safe रहाल.** Built-in firewall.
- **पैसे वाचतील.** Manupatra ₹15,000+/वर्ष vs ₹0.
- **Private रहाल.** तुमचे client matters laptop मधून बाहेर पडत नाहीत.
- **Scale करू शकता.** Solo → Firm एका command मध्ये.

## 🧠 आत 7 specialists राहतात

1. **Receptionist (मेंदू)** — तुम्ही काय बोलताय ऐकतो, योग्य specialist ला बोलवतो.
2. **Citation Clerk** — AIR/SCC/SCC OnLine ओळखतो.
3. **Court Registrar** — your High Court, Supreme Court, DRT etc. ची माहिती.
4. **Matter Manager** — प्रत्येक मॅटर ची स्वतःची memory.
5. **Drafting Assistant** — Wolfgang_rush plugins सोबत काम करतो (v0.2+).
6. **Compliance Officer** — BCI Rule 36 + DPDP firewall.
7. **Deadline Tracker** — limitation + hearing dates (v0.2+).

## 🚀 30 मिनिटात सुरुवात

### Step 1 — Python install करा
- **Mac:** [MAC_INSTALL.md](MAC_INSTALL.md)
- **Windows:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md)

### Step 2 — एका command मध्ये install

```
pip install git+https://github.com/Wolfgangrush/ai-law-firm-india.git
```

### Step 3 — AI brain जोडा

| Choice | Cost | Privacy | कोणासाठी |
|---|---|---|---|
| 🥇 **Local (Ollama + Qwen3)** | ₹0 कायमस्वरूपी | 🟢 परिपूर्ण | **client matters handle करणारे प्रत्येकजण** |
| 🥈 **DeepSeek API** | ~₹80-200/महिना | ⚠️ चांगली पण opt-out हवा | NON-client काम |
| 🥉 **Claude / Gemini API** | ~₹1500-5000/महिना | 🟢 मजबूत | Heavy daily users |

[MODEL_SETUP.md](MODEL_SETUP.md) पहा.

### Step 4 — पहिली बातचीत

```
ailawfirm-india
```

```
> tell me about your High Court
> validate AIR 1973 SC 1461
> check this language: "Best advocate in Mumbai"
> what's the limitation period for a money suit?
```

## 🛡️ Privacy ची honest बाजू

**Tool स्वतः:** सर्व data तुमच्या laptop वर `~/.ailawfirm-india/` मध्ये. कोणत्याही cloud वर upload नाही.

**Cloud AI:** Cloud API वापरल्यास queries त्यांच्या servers ला जातात. खरी client confidentiality हवी असल्यास **local Ollama** वापरा.

## 📁 Data कुठे रहातो

```
~/.ailawfirm-india/
├── palace/                ← सर्व memory
├── config.json            ← settings
└── people_map.json        ← clients साठी aliases
```

Backup: हे folder USB / Dropbox / OneDrive ला copy करा.

## 🆘 अडकलात तर

- GitHub issues: https://github.com/Wolfgangrush/ai-law-firm-india/issues
- LinkedIn community: Wolfgang_rush page

## 🙏 Credits

- **Engine:** a local memory architecture — सर्व architectural credit त्यांना.
- **Publisher:** [Wolfgang_rush](https://github.com/Wolfgangrush)
- **Author:** Rushikesh Mahajan, Advocate (your High Court Bench)

जर हे तुमचा आठवड्याचा एक तास वाचवतं, tool ने स्वतःला हजार वेळा pay केलं.

`चला सुरू करूया.` 🙏

---

**License:** MIT. **Disclaimer:** हे tool practice organize करायला मदत करतं. कायदेशीर सल्ला देत नाही. BCI Rule 36 firewall built-in आहे पण compliance ची जबाबदारी तुमची.
