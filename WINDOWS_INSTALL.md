# 🪟 Windows Install Guide — AI Brain India

Total time: ~15 minutes. You don't need to know what PowerShell is — just follow along.

---

## 🤔 What is "PowerShell"?

PowerShell is the modern Windows command-line. It's like a chat window where you type commands and the computer does them. You're going to use it 3 times in this entire install. Don't be scared — copy and paste is your friend.

**To open PowerShell:**
1. Press the Windows key on your keyboard (the one between Ctrl and Alt)
2. Type: `powershell`
3. Click "Windows PowerShell" in the results
4. A blue window opens. That's PowerShell.

---

## Step 1 — Install Python (5 minutes)

Python is the programming language this tool runs on. You install it ONCE.

1. Open your web browser, go to: **https://www.python.org/downloads/**
2. Click the big yellow "Download Python 3.13.x" button (or whatever 3.11 / 3.12 / 3.13 version is latest)
3. Open the downloaded file (usually appears in your Downloads folder)
4. **CRITICAL — on the first screen, check the box that says "Add python.exe to PATH"** ✅ (this is in small text at the bottom — DO NOT skip this; it saves you 30 minutes of trouble later)
5. Click "Install Now"
6. Wait for it to finish. Click "Close" when done.

**Verify it worked:** Open PowerShell (Windows key → type powershell → Enter), then paste:
```
python --version
```
You should see something like `Python 3.13.1`. If you see "command not found" — you didn't check the PATH box. Uninstall Python, redo step 4.

---

## Step 2 — Install AI Brain India (2 minutes)

In PowerShell, paste this and press Enter:
```
pip install git+https://github.com/Wolfgangrush/ai-law-firm-india.git
```

Wait 1-2 minutes. You'll see lots of text scrolling. When it's done you'll see your `PS C:\Users\YourName>` prompt back.

**If you see an error like "pip not recognized":**
```
python -m pip install git+https://github.com/Wolfgangrush/ai-law-firm-india.git
```
(adding `python -m` in front)

**Verify it worked:** In PowerShell, paste:
```
python -c "import ailawfirm_india; print('OK')"
```
You should see `OK`. That means the tool is installed.

---

## Step 3 — Install Git (if pip install above failed because "git" was missing)

If Step 2 errored with "git not found", install Git first:

1. Go to: **https://git-scm.com/download/win**
2. Click "Click here to download" (downloads automatically)
3. Run the installer. Click "Next" through all screens (defaults are fine).
4. After install completes, **close PowerShell and reopen it** (so it picks up Git).
5. Now try Step 2 again.

---

## Step 4 — Choose your AI brain

The tool needs to be connected to an AI model to do real work. Three honest choices:

### Option A — Run a local AI on your own computer (recommended for client work)

**Privacy: perfect. Cost: ₹0 forever. Speed: slower than cloud, but private.**

1. Go to: **https://ollama.com/download**
2. Click "Download for Windows"
3. Run the installer (defaults fine)
4. After install, open PowerShell and paste:
   ```
   ollama pull qwen3:14b
   ```
   Wait 10-20 minutes (downloads ~10 GB). This is a one-time download.
5. When done, you have an AI brain running locally. No internet needed after this.

### Option B — DeepSeek API (cheap cloud option, with mandatory privacy setup)

**Cost: ~₹80-200/month for moderate use. Privacy: GOOD ONLY IF YOU OPT OUT OF TRAINING.**

⚠️ **Important honest note:** DeepSeek may use your API inputs for training BY DEFAULT. You MUST opt out before sending any client data.

1. Go to: **https://platform.deepseek.com**
2. Sign up · top up $10-20 (~₹850-1700)
3. **Go to Settings → Privacy → turn OFF "Improve the model for everyone"** (this is the opt-out)
4. Settings → API keys → Create new key → copy the `sk-...` string
5. See [MODEL_SETUP.md](MODEL_SETUP.md) for connecting it.

### Option C — Claude API or Gemini API (expensive but strong)

See [MODEL_SETUP.md](MODEL_SETUP.md).

---

## Step 5 — Run the tool

In PowerShell:
```
ailawfirm-india
```

You should see the welcome banner. Type `help` or just start asking questions:
```
> tell me about your High Court
> validate AIR 1973 SC 1461
> check this language: "Best advocate in Mumbai"
```

---

## 📁 Where your data lives on Windows

```
C:\Users\YourName\.ailawfirm-india\
├── palace\                   ← all your matter/client/citation memory
├── config.json               ← which AI model you've connected
└── people_map.json           ← optional client/party alias system
```

**To backup:** In File Explorer, navigate to `C:\Users\YourName\` (replace YourName with your actual Windows username). You'll see a folder called `.ailawfirm-india` (the dot prefix means "hidden" — make sure "Show hidden files" is on in File Explorer's View menu). Copy this folder to OneDrive, Dropbox, or a USB drive.

**To find your Windows username:** open PowerShell and type:
```
echo $env:USERNAME
```

---

## 🆘 Common Windows problems + fixes

### "pip is not recognized"
Use `python -m pip` instead of `pip`. See Step 2.

### "Permission denied" during install
PowerShell needs admin rights ONCE for the install. Close PowerShell, then:
1. Windows key → type `powershell`
2. Right-click "Windows PowerShell" → "Run as administrator"
3. Click Yes on the UAC prompt
4. Re-run Step 2

### "ailawfirm-india not recognized" after install
Add Python Scripts to PATH:
1. Press Windows key, type `environment variables`, click "Edit the system environment variables"
2. Click "Environment Variables..." button
3. Under "User variables", select "Path" → Edit → New
4. Add: `C:\Users\YourName\AppData\Local\Programs\Python\Python313\Scripts\` (adjust Python version)
5. OK, OK, OK. Close PowerShell, reopen.

### "ssl certificate" errors
You're probably behind a corporate firewall. Try:
```
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org git+https://github.com/Wolfgangrush/ai-law-firm-india.git
```

### Antivirus blocks Python
Some antivirus tools (Avast, McAfee) block pip installs of unknown packages. Temporarily disable real-time scanning for the install, then turn it back on.

---

## 🪟 Windows-specific notes

- **File paths use backslashes** on Windows (`C:\Users\...`) but the tool also accepts forward slashes (`/Users/...`).
- **Hidden files:** the `.ailawfirm-india` folder starts with a dot. Windows hides dotfiles by default. Turn on "Show hidden files" in File Explorer → View menu.
- **Encoding:** the tool uses UTF-8 throughout. If you see weird characters (`?` or boxes) when typing Hindi/Marathi/regional language, run `chcp 65001` in PowerShell before launching the tool — this sets UTF-8 mode.
- **Long paths:** if your Windows username is very long or your folder structure deep, you may hit Windows 260-character path limits. Move your install to a shorter path (e.g., `C:\dev\`) if you see "path too long" errors.

---

## Done?

Go to [GETTING_STARTED.md](GETTING_STARTED.md) for your first 30-minute tour of the tool.

If something doesn't work, file an issue at: https://github.com/Wolfgangrush/ai-law-firm-india/issues
