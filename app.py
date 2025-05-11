import tkinter as tk
from tkinter import messagebox
from password_generator import generate_password
from crypto_utils import encrypt, decrypt
from storage import save_encrypted_entry, load_data

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.configure(bg="lightblue")

        self.master_password = tk.StringVar()
        self.site = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="Master Password:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.master_password, show='*').grid(row=0, column=1)

        tk.Label(self.root, text="Site:").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.site).grid(row=1, column=1)

        tk.Label(self.root, text="Username:").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.username).grid(row=2, column=1)

        tk.Label(self.root, text="Password:").grid(row=3, column=0)
        tk.Entry(self.root, textvariable=self.password).grid(row=3, column=1)

        tk.Button(self.root, text="Generate", command=self.generate).grid(row=3, column=2)
        tk.Button(self.root, text="Save", command=self.save).grid(row=4, column=1)
        tk.Button(self.root, text="Show Saved", command=self.show_saved).grid(row=5, column=1)

        tk.Label(self.root, text="🔒 Created by Maciej Zareba", font=("Arial", 10), bg="lightblue", fg="gray").grid(row=6, column=0, columnspan=3, pady=10)

    def generate(self):
        self.password.set(generate_password())

    def save(self):
        try:
            encrypted_pw = encrypt(self.password.get(), self.master_password.get())
            save_encrypted_entry(self.site.get(), self.username.get(), encrypted_pw)
            messagebox.showinfo("Success", "Password saved.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_saved(self):
        try:
            data = load_data()
            display = ""
            for site, entry in data.items():
                try:
                    decrypted_pw = decrypt(entry["password"], self.master_password.get())
                    display += f"{site} - {entry['username']} : {decrypted_pw}\n"
                except:
                    display += f"{site} - {entry['username']} : [Wrong Master Password or Corrupted]\n"
            messagebox.showinfo("Saved Passwords", display)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
