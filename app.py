import tkinter as tk
from tkinter import messagebox

from model import SmartTextAI


# -----------------------------
# Load Transformer
# -----------------------------

ai = SmartTextAI()


# -----------------------------
# Analyze Function
# -----------------------------

def analyze_text():

    text = text_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning(
            "Warning",
            "Please enter some text."
        )
        return

    label, confidence = ai.analyze(text)

    confidence_percent = confidence * 100

    if label == "POSITIVE":
        emoji = "😊"
    else:
        emoji = "😞"

    result_label.config(
        text=f"{emoji} {label}\nConfidence: {confidence_percent:.2f}%"
    )


def clear_text():

    text_box.delete("1.0", tk.END)

    result_label.config(
        text="Result will appear here"
    )


# -----------------------------
# GUI
# -----------------------------

root = tk.Tk()

root.title("SmartText AI")
root.geometry("750x550")

root.configure(bg="#111827")


# -----------------------------
# Title
# -----------------------------

title = tk.Label(
    root,
    text="SmartText AI",
    font=("Arial", 28, "bold"),
    fg="white",
    bg="#111827"
)

title.pack(pady=25)


subtitle = tk.Label(
    root,
    text="Transformer-Based Text Intelligence",
    font=("Arial", 13),
    fg="#9CA3AF",
    bg="#111827"
)

subtitle.pack()


# -----------------------------
# Input
# -----------------------------

text_box = tk.Text(
    root,
    height=8,
    width=70,
    font=("Arial", 13),
    bg="#1F2937",
    fg="white",
    insertbackground="white",
    relief="flat",
    padx=15,
    pady=15
)

text_box.pack(pady=25)


# -----------------------------
# Analyze Button
# -----------------------------

analyze_button = tk.Button(
    root,
    text="Analyze Text",
    command=analyze_text,
    font=("Arial", 13, "bold"),
    bg="#2563EB",
    fg="white",
    padx=25,
    pady=10,
    relief="flat",
    cursor="hand2"
)

analyze_button.pack()


# -----------------------------
# Clear Button
# -----------------------------

clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_text,
    font=("Arial", 11),
    bg="#374151",
    fg="white",
    padx=20,
    pady=7,
    relief="flat"
)

clear_button.pack(pady=10)


# -----------------------------
# Result
# -----------------------------

result_label = tk.Label(
    root,
    text="Result will appear here",
    font=("Arial", 18, "bold"),
    fg="#22C55E",
    bg="#111827"
)

result_label.pack(pady=30)


# -----------------------------
# Run
# -----------------------------

root.mainloop()