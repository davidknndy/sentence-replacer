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
    try:
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
    except Exception as e:
        print(f"❌ Unexpected error in improve_clipboard_text: {e}")

# Use the external icon file for the systray icon
ICON_PATH = "text.ico"

def on_exit(icon, item):
    try:
        icon.stop()
        print("👋 Exiting...")
        keyboard.unhook_all_hotkeys()
    except Exception as e:
        print(f"❌ Error during exit: {e}")

def hotkey_thread():
    keyboard.add_hotkey('ctrl+alt+s', improve_clipboard_text)
    keyboard.wait('esc')

def load_icon_from_ico(path):
    # Load .ico file as PIL Image for pystray
    if not os.path.exists(path):
        raise FileNotFoundError(f"Icon file not found: {path}")
    return Image.open(path)

if __name__ == "__main__":
    print("📋 Clipboard grammar fixer ready.")
    print("👉 Copy any text, press Ctrl+Alt+S to fix. Press ESC to exit or use the tray icon.")

    # Start hotkey listener in a background thread
    threading.Thread(target=hotkey_thread, daemon=True).start()

    # Load the .ico file as a PIL Image for pystray
    icon_image = load_icon_from_ico(ICON_PATH)

    # Run the tray icon in the main thread, only with Exit option
    icon = pystray.Icon(
        "SentenceReplacer",
        icon_image,
        "SentenceReplacer",
        menu=pystray.Menu(
            pystray.MenuItem("Exit", on_exit)
        )
    )
    icon.run()
