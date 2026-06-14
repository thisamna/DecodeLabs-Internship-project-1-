import tkinter as tk
from datetime import datetime


def get_response(msg):
    msg = msg.lower()

    if any(word in msg for word in ["hi", "hello", "hey"]):
        return "Hello. How can I help you today?"

    elif "how are you" in msg:
        return "I am functioning properly. How can I assist you?"

    elif any(word in msg for word in ["study", "university", "college", "exam", "assignment", "homework"]):
        return "Focus is important. Take regular breaks and stay consistent."

    elif any(word in msg for word in ["stress", "tired", "pressure", "anxious"]):
        return "Try to stay calm and manage your workload step by step."

    elif "time" in msg or "current time" in msg or "what time" in msg:
        return "Current Time: " + datetime.now().strftime("%I:%M %p")

    elif "date" in msg or "today date" in msg:
        return "Today's Date: " + datetime.now().strftime("%d-%m-%Y")

    elif any(word in msg for word in ["bye", "exit", "goodbye", "see you", "take care"]):
        return "Goodbye. Have a good day."

    else:
        return "I did not understand your request. Please rephrase it."


def add_message(text, sender):
    container = tk.Frame(chat_frame, bg="#f8fafc")

    if sender == "user":
        bg = "#1e3a8a"
        fg = "white"
        side = "e"
    else:
        bg = "#e2e8f0"
        fg = "#0f172a"
        side = "w"

    bubble = tk.Label(
        container,
        text=text,
        bg=bg,
        fg=fg,
        font=("Segoe UI", 10),
        wraplength=420,
        justify="left",
        padx=12,
        pady=8
    )

    bubble.pack(anchor=side, pady=5, padx=10)
    container.pack(fill="both", anchor=side)


def send(event=None):
    msg = entry.get("1.0", tk.END).strip()
    if not msg:
        return

    add_message(msg, "user")
    add_message(get_response(msg), "bot")

    entry.delete("1.0", tk.END)
    canvas.yview_moveto(1.0)


root = tk.Tk()
root.title("DecodeBot AI")
root.geometry("900x700")
root.configure(bg="#f8fafc")

header = tk.Frame(root, bg="#1e3a8a", height=55)
header.pack(fill="x")

title = tk.Label(
    header,
    text="DecodeBot AI Chat",
    bg="#1e3a8a",
    fg="white",
    font=("Segoe UI", 14, "bold")
)
title.pack(side="left", padx=15, pady=12)

status = tk.Label(
    header,
    text="● Online",
    bg="#1e3a8a",
    fg="#dbeafe",
    font=("Segoe UI", 10)
)
status.pack(side="right", padx=15)

canvas = tk.Canvas(root, bg="#f8fafc", highlightthickness=0)
chat_frame = tk.Frame(canvas, bg="#f8fafc")

scroll = tk.Scrollbar(root, command=canvas.yview)
canvas.configure(yscrollcommand=scroll.set)

scroll.pack(side="right", fill="y")
canvas.pack(fill="both", expand=True)

canvas.create_window((0, 0), window=chat_frame, anchor="nw")


def update_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


chat_frame.bind("<Configure>", update_scroll)

bottom = tk.Frame(root, bg="#ffffff")
bottom.pack(fill="x")

entry = tk.Text(
    bottom,
    height=2,
    font=("Segoe UI", 11),
    bg="#ffffff",
    fg="#0f172a",
    insertbackground="#1e3a8a"
)
entry.pack(side="left", fill="x", expand=True, padx=10, pady=10)

send_btn = tk.Button(
    bottom,
    text="Send",
    command=send,
    bg="#1e3a8a",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    padx=18,
    pady=6,
    relief="flat",
    activebackground="#0f2f6b"
)
send_btn.pack(side="right", padx=10)

entry.bind("<Return>", send)

add_message("Hello. I am DecodeBot AI. Start chatting.", "bot")

root.mainloop()