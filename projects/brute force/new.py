import tkinter as tk
from tkinter import messagebox
import time

class LoginBruteForceSimulator(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Login Simulator")
        self.geometry("400x250")
        self.resizable(False, False)

        self.correct_username = "admin"
        self.correct_password = "password123"
        self.failed_attempts = 0
        self.lockout_time = 60 
        self.is_locked = False

        self.create_widgets()

    def create_widgets(self):
  
        self.main_frame = tk.Frame(self, padx=20, pady=20)
        self.main_frame.pack(expand=True)

        # Username
        self.username_label = tk.Label(self.main_frame, text="Username:")
        self.username_label.grid(row=0, column=0, sticky="w", pady=5)
        self.username_entry = tk.Entry(self.main_frame, width=30)
        self.username_entry.grid(row=0, column=1, pady=5)

        # Password
        self.password_label = tk.Label(self.main_frame, text="Password:")
        self.password_label.grid(row=1, column=0, sticky="w", pady=5)
        self.password_entry = tk.Entry(self.main_frame, show="*", width=30)
        self.password_entry.grid(row=1, column=1, pady=5)

        # Login Button
        self.login_button = tk.Button(self.main_frame, text="Login", command=self.check_login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Message Label
        self.message_label = tk.Label(self.main_frame, text="", fg="red")
        self.message_label.grid(row=3, column=0, columnspan=2, pady=5)

    def check_login(self):
  
        if self.is_locked:
            return

        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == self.correct_username and password == self.correct_password:
            messagebox.showinfo("Success", "Login successful! Welcome.")
            self.destroy() 
        else:
            self.failed_attempts += 1
            remaining_attempts = 3 - self.failed_attempts
            if remaining_attempts > 0:
                self.message_label.config(text=f"Invalid credentials. {remaining_attempts} attempts left.")
            else:
                self.lock_account()

    def lock_account(self):
        """Locks the account after too many failed attempts."""
        self.is_locked = True
        self.login_button.config(state=tk.DISABLED)
        self.message_label.config(text=f"Too many failed attempts.")
        self.countdown(self.lockout_time)

    def countdown(self, remaining):
        """Handles the lockout countdown timer."""
        if remaining > 0:
            self.message_label.config(text=f"Account locked for {remaining} seconds.")
            self.after(1000, self.countdown, remaining - 1)
        else:
            self.unlock_account()

    def unlock_account(self):
        """Unlocks the account after the lockout period."""
        self.is_locked = False
        self.failed_attempts = 0
        self.login_button.config(state=tk.NORMAL)
        self.message_label.config(text="Account unlocked. Please try again.")

if __name__ == "__main__":
    app = LoginBruteForceSimulator()
    app.mainloop()