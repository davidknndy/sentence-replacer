# ✨ Sentence Replacer – Clipboard Grammar Fixer

A simple and powerful Python tool that improves your writing almost instantly using ChatGPT.  
Just copy any text, press `Ctrl + Alt + S`, and your clipboard will be replaced with a clearer, more professional version, ready to paste.

---

## 📸 Demo

| Original | Action | Result |
|----------|--------|--------|
| ![Original](https://i.ibb.co/Mx0yT5JC/orig.png) | ![Hotkey](https://i.ibb.co/vC2j0Nkg/copied.png) | ![Improved](https://i.ibb.co/jkTk02Lr/new.png) |

---

## 🧠 How It Works

1. Select any text and copy it (`Ctrl + C`)
2. Press `Ctrl + Alt + S`
3. The app sends your text to **ChatGPT** to fix grammar and clarity
4. The polished version is copied back to your clipboard
5. Just paste it (`Ctrl + V`) wherever you want

---

## 🚀 Features

- 🔥 Works entirely through hotkeys (no interface)
- ✅ Almost Instant grammar and clarity improvement via OpenAI API
- 📋 Replaces clipboard content automatically
- 🖥️ Runs silently in the system tray (`.pyw` version)
- 🔐 Keeps your API key safe via `.env`

---

## 💻 Installation (Windows)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/sentence-replacer.git
cd sentence-replacer
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Add Your OpenAI API Key

Create a file called `.env` in the project root. Paste the following line into it (replace with your real key):

```env
OPEN_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

❗ **Important:** This file is already included in `.gitignore` so your key won't be uploaded to GitHub.

---

## ▶️ Running the App

**To run with console (shows logs/output):**

```bash
python sentencereplacer.py
```

**To run silently in the background with system tray icon:**

```bash
pythonw SentReplacer.pyw
```

In tray mode, you can right-click the icon and select Exit, or press `Esc` on your keyboard.

---

## 📁 File Structure

```
sentence-replacer/
├── sentencereplacer.py      # Main script (with terminal output)
├── SentReplacer.pyw         # Silent tray version (no console)
├── requirements.txt         # Dependencies
├── .gitignore               # Ignores .env and unnecessary files
├── .env                     # Contains your OpenAI API key (NOT uploaded)
├── text.ico                 # Icon for system tray
├── README.md
```

---

## 📦 Requirements

This app uses the following libraries:

- openai
- pyperclip
- keyboard
- pystray
- Pillow
- python-dotenv

Install them all via:

```bash
pip install -r requirements.txt
```

---

Made with ❤️ to help you write better, faster.