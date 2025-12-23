import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import pyttsx3

# ---------- TTS SETUP ----------
engine = pyttsx3.init()          # offline TTS engine [web:26]
engine.setProperty("rate", 170)  # speaking speed
engine.setProperty("volume", 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------- SIMPLE BOT LOGIC ----------
def bot_reply(user_text: str) -> str:
    text = user_text.lower().strip()
    if not text:
        return "Say something, I am listening!"
    if "hello" in text or "hi" in text:
        return "Hey, nice to see you!"
    if "name" in text:
        return "I am your Python avatar buddy."
    if "bye" in text:
        return "Bye! See you soon."
    # default
    return "Interesting! Tell me more."

# ---------- GUI ----------
root = tk.Tk()
root.title("Talking Avatar")

# load avatar image
avatar_img = Image.open("anime-boy-avatar-isolated-vector.jpg")  # your file [file:1]
avatar_img = avatar_img.resize((250, 250))
avatar_photo = ImageTk.PhotoImage(avatar_img)  # [web:38]

avatar_label = tk.Label(root, image=avatar_photo)
avatar_label.grid(row=0, column=0, padx=10, pady=10, rowspan=2)

chat_box = scrolledtext.ScrolledText(root, width=40, height=15, state="disabled", wrap="word")
chat_box.grid(row=0, column=1, padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.grid(row=1, column=1, padx=10, pady=10, sticky="we")

def add_chat(sender, text):
    chat_box.configure(state="normal")
    chat_box.insert(tk.END, f"{sender}: {text}\n")
    chat_box.configure(state="disabled")
    chat_box.see(tk.END)

def on_send(event=None):
    user_text = entry.get()
    if not user_text.strip():
        return
    entry.delete(0, tk.END)

    add_chat("You", user_text)

    reply = bot_reply(user_text)
    add_chat("Avatar", reply)

    # simple "animation": flash avatar bg while speaking
    avatar_label.config(bg="#ffeaa7")
    root.update_idletasks()

    speak(reply)

    avatar_label.config(bg=root.cget("bg"))

send_btn = tk.Button(root, text="Send", command=on_send)
send_btn.grid(row=2, column=1, padx=10, pady=(0, 10), sticky="e")

entry.bind("<Return>", on_send)

root.mainloop()
