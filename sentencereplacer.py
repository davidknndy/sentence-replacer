# Created and developed by David Kennedy

import openai
import pyperclip
import keyboard
import threading
import pystray
from PIL import Image, ImageDraw
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")

# Create a client using the correct method for openai >= 1.0.0
client = openai.OpenAI(api_key=OPEN_API_KEY)

def improve_clipboard_text():
    original_text = pyperclip.paste()

    if not original_text.strip():
        print("⚠️ Clipboard is empty or just whitespace.")
        return

    print(f"🔍 Original:\n{original_text}\n")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Or "gpt-4.1-mini"
            messages=[
                {"role": "user", "content": f"Fix grammar and clarity of this:\n\n{original_text}"}
            ],
            temperature=0.3
        )
        improved_text = response.choices[0].message.content.strip()
        pyperclip.copy(improved_text)
        print("✅ Improved text copied to clipboard.")
    except Exception as e:
        print(f"❌ API Error: {e}")

def create_image():
    # Simple icon: white "SR" on blue background
    img = Image.new('RGB', (64, 64), color=(40, 80, 200))
    d = ImageDraw.Draw(img)
    d.text((16, 16), "SR", fill=(255, 255, 255))
    return img

def on_improve(icon, item):
    improve_clipboard_text()

def on_exit(icon, item):
    icon.stop()
    print("👋 Exiting...")
    keyboard.unhook_all_hotkeys()

def systray_thread():
    icon = pystray.Icon(
        "SentenceReplacer",
        create_image(),
        "SentenceReplacer",
        menu=pystray.Menu(
            pystray.MenuItem("Improve Clipboard", on_improve),
            pystray.MenuItem("Exit", on_exit)
        )
    )
    icon.run()

if __name__ == "__main__":
    print("📋 Clipboard grammar fixer ready.")
    print("👉 Copy any text, press Ctrl+Alt+S to fix. Press ESC to exit or use the tray icon.")

    # Start systray in a separate thread
    threading.Thread(target=systray_thread, daemon=True).start()

    # Register hotkey
    keyboard.add_hotkey('ctrl+alt+s', improve_clipboard_text)

    # Wait for ESC to exit
    keyboard.wait('esc')
