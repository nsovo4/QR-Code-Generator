import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import qrcode
import os

class QRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        self.file_path = None

        self.label = tk.Label(root, text="Enter a URL or select a file", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=50, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.select_file_btn = tk.Button(root, text="Browse File (Image/PDF)", command=self.browse_file)
        self.select_file_btn.pack(pady=5)

        self.generate_btn = tk.Button(root, text="Generate QR Code", bg="green", fg="white", command=self.generate_qr)
        self.generate_btn.pack(pady=20)

        self.qr_label = tk.Label(root)
        self.qr_label.pack(pady=10)

        self.save_btn = tk.Button(root, text="Save QR Code", command=self.save_qr)
        self.save_btn.pack(pady=5)

    def browse_file(self):
        file_types = [("PDF or Images", "*.pdf *.png *.jpg *.jpeg *.gif")]
        file = filedialog.askopenfilename(filetypes=file_types)
        if file:
            self.file_path = file
            self.entry.delete(0, tk.END)
            self.entry.insert(0, file)

    def generate_qr(self):
        data = self.entry.get().strip()
        if not data:
            messagebox.showwarning("Missing Input", "Please enter a URL or select a file.")
            return

        qr = qrcode.make(data)
        self.qr_img = qr
        qr = qr.resize((250, 250))
        self.tk_img = ImageTk.PhotoImage(qr)
        self.qr_label.config(image=self.tk_img)
        messagebox.showinfo("Success", "QR code generated!")

    def save_qr(self):
        if not hasattr(self, 'qr_img'):
            messagebox.showwarning("No QR Code", "Generate a QR code first.")
            return

        file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file:
            self.qr_img.save(file)
            messagebox.showinfo("Saved", f"QR Code saved as:\n{file}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRApp(root)
    root.mainloop()
