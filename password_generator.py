import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("420x260")
        self.root.resizable(False, False)

        self.length_var = tk.IntVar(value=12)
        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        self.password_var = tk.StringVar()

        ttk.Label(root, text="Password Length:", font=("Segoe UI", 11)).pack(pady=(15, 0))
        length_spin = ttk.Spinbox(root, from_=4, to=64, textvariable=self.length_var, width=5)
        length_spin.pack()

        options_frame = ttk.LabelFrame(root, text="Include Characters", padding=10)
        options_frame.pack(padx=15, pady=15, fill="x")

        ttk.Checkbutton(options_frame, text="Uppercase (A-Z)", variable=self.use_upper).grid(row=0, column=0, sticky="w")
        ttk.Checkbutton(options_frame, text="Lowercase (a-z)", variable=self.use_lower).grid(row=1, column=0, sticky="w")
        ttk.Checkbutton(options_frame, text="Digits (0-9)", variable=self.use_digits).grid(row=0, column=1, sticky="w")
        ttk.Checkbutton(options_frame, text="Symbols (!@#$)", variable=self.use_symbols).grid(row=1, column=1, sticky="w")

        ttk.Button(root, text="Generate Password", command=self.generate_password).pack(pady=5)

        out_entry = ttk.Entry(root, textvariable=self.password_var, font=("Consolas", 12), width=30, state="readonly")
        out_entry.pack(pady=(5, 2))

        ttk.Button(root, text="Copy to Clipboard", command=self.copy_password).pack()

    def generate_password(self):
        length = self.length_var.get()
        char_pools = ""

        if self.use_upper.get():
            char_pools += string.ascii_uppercase
        if self.use_lower.get():
            char_pools += string.ascii_lowercase
        if self.use_digits.get():
            char_pools += string.digits
        if self.use_symbols.get():
            char_pools += string.punctuation

        if not char_pools:
            messagebox.showwarning("No character set selected", "Please select at least one character type.")
            return

        password_chars = []
        if self.use_upper.get():
            password_chars.append(random.choice(string.ascii_uppercase))
        if self.use_lower.get():
            password_chars.append(random.choice(string.ascii_lowercase))
        if self.use_digits.get():
            password_chars.append(random.choice(string.digits))
        if self.use_symbols.get():
            password_chars.append(random.choice(string.punctuation))

        remaining_len = length - len(password_chars)
        password_chars += random.choices(char_pools, k=remaining_len)
        random.shuffle(password_chars)
        self.password_var.set("".join(password_chars))

    def copy_password(self):
        pw = self.password_var.get()
        if pw:
            self.root.clipboard_clear()
            self.root.clipboard_append(pw)
            messagebox.showinfo("Copied", "Password copied to clipboard.")

if __name__ == "__main__":
    app_root = tk.Tk()
    PasswordGeneratorApp(app_root)
    app_root.mainloop()
