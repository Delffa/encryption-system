import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from crypto_engine import CryptoEngine

class App:

    def __init__(self, root):

        self.root = root

        root.title("AegisCrypt")

        tk.Label(root,text="Parola").pack()

        self.password = tk.Entry(
            root,
            show="*",
            width=40
        )

        self.password.pack()

        tk.Button(
            root,
            text="Dosya Şifrele",
            command=self.encrypt
        ).pack(pady=5)

        tk.Button(
            root,
            text="Dosya Çöz",
            command=self.decrypt
        ).pack(pady=5)

    def encrypt(self):

        file = filedialog.askopenfilename()

        if not file:
            return

        CryptoEngine.encrypt_file(
            file,
            self.password.get()
        )

        messagebox.showinfo(
            "Başarılı",
            "Dosya şifrelendi"
        )

    def decrypt(self):

        file = filedialog.askopenfilename()

        if not file:
            return

        CryptoEngine.decrypt_file(
            file,
            self.password.get()
        )

        messagebox.showinfo(
            "Başarılı",
            "Dosya çözüldü"
        )
