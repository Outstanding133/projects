import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

def calculate_sha256(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

class FileIntegrityChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("File Integrity Checker")
        self.root.geometry("500x300")
        self.file_path = None
        self.saved_hash = None

        self.label = tk.Label(root, text="No file selected")
        self.label.pack(pady=10)

        self.hash_text = tk.Text(root, height=5, width=60)
        self.hash_text.pack(pady=10)

        tk.Button(root, text="Select File", command=self.select_file).pack(pady=5)
        tk.Button(root, text="Generate Hash", command=self.generate_hash).pack(pady=5)
        tk.Button(root, text="Re-check Integrity", command=self.recheck_integrity).pack(pady=5)

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        self.label.config(text=f"Selected File: {self.file_path}")

    def generate_hash(self):
        if not self.file_path:
            messagebox.showwarning("Warning", "Please select a file first.")
            return

        self.saved_hash = calculate_sha256(self.file_path)
        self.hash_text.delete("1.0", tk.END)
        self.hash_text.insert(tk.END, f"SHA-256 Hash:\n{self.saved_hash}")

    def recheck_integrity(self):
        if not self.file_path or not self.saved_hash:
            messagebox.showwarning("Warning", "No file or hash to compare.")
            return

        current_hash = calculate_sha256(self.file_path)
        if current_hash == self.saved_hash:
            messagebox.showinfo("Result", "✅ File integrity verified. No changes detected.")
        else:
            messagebox.showerror("Result", "❌ File has been modified!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileIntegrityChecker(root)
    root.mainloop()
