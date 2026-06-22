# 🙏 স্বাগতম, অ্যাডভোকেট সাহেব — আপনার AI Brain এখান থেকে শুরু

> ⚠️ **এই অনুবাদ AI-সহায়তায় তৈরি।** যদি কোনো শব্দ বা বাক্য ভুল মনে হয়, অনুগ্রহ করে [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) দেখুন এবং সংশোধনের জন্য GitHub-এ Pull Request পাঠান।

আপনাকে programmer হতে হবে না। Mac কিনতে হবে না। কোনো subscription লাগবে না। আপনার দরকার — একটি Windows laptop বা Mac, internet (শুধু install-এর জন্য), এবং ৩০ মিনিট।

যদি copy-paste করতে পারেন, তবে এটি চালাতে পারবেন।

> **English:** [GETTING_STARTED.md](GETTING_STARTED.md) · **हिन्दी:** [GETTING_STARTED_HINDI.md](GETTING_STARTED_HINDI.md) · **मराठी:** [GETTING_STARTED_MARATHI.md](GETTING_STARTED_MARATHI.md)
> **Windows install:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md) · **Mac install:** [MAC_INSTALL.md](MAC_INSTALL.md) · **AI মডেল সংযোগ:** [MODEL_SETUP.md](MODEL_SETUP.md)

---

## ✨ এটি কী, এক অনুচ্ছেদে

একটি ফ্রি tool যা আপনার laptop-কে একটি ছোট ব্যক্তিগত আইনি office assistant-এ পরিণত করে। এটি আপনার সমস্ত matter মনে রাখে (প্রতিটি case file, পক্ষ, order, hearing-এর তারিখ)। এটি ভারতীয় legal citations parse করে (AIR · SCC · SCC OnLine)। কোন court-এর কোথায় jurisdiction তা বলে দেয়। BCI Rule 36 ঝুঁকি flag করে। এটি **আপনার নিজের computer-এ** চলে — cloud নেই, upload নেই, তৃতীয় পক্ষ আপনার client-এর data পড়তে পারে না। Open-source (MIT license)।

## 💛 ভারতের solo অ্যাডভোকেটদের জন্য কেন

- **কম ভুলবেন** — মাসের পুরনো matter-এর context তৎক্ষণাৎ ফিরে আসে।
- **Deadline কম miss হবে** — hearing dates ও limitation periods track হয়।
- **BCI Rule 36 safe** — built-in firewall publishing-এর আগে আপনার ভাষা পরীক্ষা করে।
- **টাকা বাঁচবে** — Manupatra ₹15,000+/বছর। এটি ₹0।
- **Private থাকবেন** — client matter laptop থেকে বের হয় না।

## 🧠 ভেতরে ৭ জন specialist থাকে

| # | Specialist | যা করে |
|---|---|---|
| 🧠 | **Receptionist (মস্তিষ্ক)** | আপনি যা বলেন শোনে · সঠিক specialist-কে ডাকে |
| 📂 | **Matter Manager** | প্রতিটি active case file ধারণ করে |
| 📜 | **Citation Clerk** | AIR/SCC/SCC OnLine parse করে |
| 🏛️ | **Court Registrar** | court-এর তথ্য · jurisdiction |
| ✍️ | **Drafting Assistant** | Wolfgang_rush plugins-এর সাথে |
| 🛡️ | **Compliance Officer** | BCI Rule 36 + DPDP firewall |
| 📅 | **Deadline Tracker** | limitation + hearing dates |

আপনি শুধু Receptionist-এর সাথে কথা বলেন। বাকিরা পেছনে কাজ করে।

## 🚀 ৩০ মিনিটে শুরু

### Step 1 — Python install
- **Mac:** [MAC_INSTALL.md](MAC_INSTALL.md) দেখুন
- **Windows:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md) দেখুন

### Step 2 — Tool install

Terminal (Mac) বা PowerShell (Windows) খুলে paste করুন:

```
pip install git+https://github.com/Wolfgangrush/ai-law-firm-india.git
```

### Step 3 — AI brain সংযোগ

| Choice | Cost | Privacy | কার জন্য |
|---|---|---|---|
| 🥇 **Local (Ollama + Qwen3)** | ₹0 চিরকাল | 🟢 নিখুঁত | **client matter handle করেন এমন সবাই** |
| 🥈 **DeepSeek API** | ~₹৮০-২০০/মাস | ⚠️ ভাল কিন্তু opt-out দরকার | client নয় এমন কাজ |
| 🥉 **Claude / Gemini API** | ~₹১৫০০-৫০০০/মাস | 🟢 শক্তিশালী | heavy daily users |

[MODEL_SETUP.md](MODEL_SETUP.md) দেখুন।

### Step 4 — প্রথম কথোপকথন

```
ailawfirm-india
```

চেষ্টা করুন:
```
> tell me about Calcutta High Court
> validate AIR 1973 SC 1461
> check this language: "Best advocate in Kolkata"
> what's the limitation period for a money suit?
```

## 🛡️ Privacy-এর সৎ কথা

**Tool নিজে:** সমস্ত data আপনার laptop-এ `~/.ailawfirm-india/` folder-এ। কোনো cloud-এ upload হয় না।

**Cloud AI:** cloud API ব্যবহার করলে query তাদের server-এ যায়। প্রকৃত client গোপনীয়তার জন্য **local Ollama** ব্যবহার করুন।

## 📁 Data কোথায় থাকে

```
~/.ailawfirm-india/                  ← Mac
C:\Users\YourName\.ailawfirm-india\  ← Windows
├── palace/                          ← সমস্ত memory
├── config.json                      ← আপনার settings
└── people_map.json                  ← optional alias
```

Backup: এই folder USB / Dropbox / OneDrive-এ copy করুন।

## 🙏 Credits

- **Engine:** a local memory architecture — সমস্ত architectural credit তাদের।
- **Publisher:** [Wolfgang_rush](https://github.com/Wolfgangrush)
- **Author:** Rushikesh Mahajan, Advocate (your High Court Bench)

যদি এটি আপনার সপ্তাহের একটি ঘন্টা বাঁচায়, tool নিজেকে হাজার বার pay করেছে।

`চলুন শুরু করি।` 🙏

---

**License:** MIT। **Disclaimer:** এই tool আপনার practice organize করতে সাহায্য করে। এটি আইনি পরামর্শ দেয় না। BCI Rule 36 firewall built-in কিন্তু compliance-এর দায়িত্ব আপনার।

**সংশোধন/উন্নতির জন্য:** [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) দেখুন।
