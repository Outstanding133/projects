import tkinter as tk
from tkinter import messagebox, filedialog, font
import os


def encrypt(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, key):
    return encrypt(text, -key)


def save_note():
    note = text_area.get("1.0", tk.END).strip()
    password = password_entry.get()

    if not note or not password:
        messagebox.showwarning("Input Error", "Both Note and Password are required.")
        return

    try:
        key = int(password)
    except ValueError:
        messagebox.showerror("Key Error", "Password must be a number for Caesar Cipher.")
        return

    encrypted = encrypt(note, key)
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    
    if filepath:
        with open(filepath, "w") as file:
            file.write(encrypted)
        messagebox.showinfo("Success", f"Note saved and encrypted successfully!")


def open_note():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not filepath:
        return

    password = password_entry.get()
    if not password:
        messagebox.showwarning("Password Needed", "Enter password to decrypt the file.")
        return

    try:
        key = int(password)
    except ValueError:
        messagebox.showerror("Key Error", "Password must be a number for Caesar Cipher.")
        return

    with open(filepath, "r") as file:
        encrypted = file.read()

    decrypted = decrypt(encrypted, key)
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, decrypted)
    messagebox.showinfo("Success", f"Note decrypted successfully!")


app = tk.Tk()
app.title("🔐 Secure Note Taker")
app.geometry("500x500")
app.config(padx=20, pady=20)


tk.Label(app, text="Enter your note:", font=("Poppins", 14)).pack(anchor="w")
text_area = tk.Text(app, height=15, wrap=tk.WORD, font=("Poppins", 12))
text_area.pack(pady=10, fill="both", expand=True)

tk.Label(app, text="Encryption Password (Number):", font=("Poppins", 12)).pack(anchor="w")
password_entry = tk.Entry(app, show="*", font=("Poppins", 12))
password_entry.pack(fill="x", pady=5)


frame = tk.Frame(app)
frame.pack(pady=10)

tk.Button(frame, text="💾 Save Note", font=("Poppins", 12), command=save_note).grid(row=0, column=0, padx=10)
tk.Button(frame, text="📂 Open Note", font=("Poppins", 12), command=open_note).grid(row=0, column=1, padx=10)


app.mainloop()
