import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import qrcode

class QRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("500x550")
        self.root.resizable(False, False)

        self.label = tk.Label(root, text="Enter a URL or text", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=50, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.generate_btn = tk.Button(root, text="Generate QR Code", bg="green", fg="white", command=self.generate_qr)
        self.generate_btn.pack(pady=20)

        self.qr_label = tk.Label(root)
        self.qr_label.pack(pady=10)

        self.save_btn = tk.Button(root, text="Save QR Code", command=self.save_qr)
        self.save_btn.pack(pady=5)

    def generate_qr(self):
        data = self.entry.get().strip()
        if not data:
            messagebox.showwarning("Input Required", "Please enter some text or a URL.")
            return

        qr = qrcode.make(data)
        self.qr_img = qr
        qr = qr.resize((250, 250))
        self.tk_img = ImageTk.PhotoImage(qr)
        self.qr_label.config(image=self.tk_img)
        messagebox.showinfo("Success", "QR Code generated!")

    def save_qr(self):
        if not hasattr(self, 'qr_img'):
            messagebox.showwarning("No QR Code", "Please generate a QR Code first.")
            return

        file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file:
            self.qr_img.save(file)
            messagebox.showinfo("Saved", f"QR Code saved at:\n{file}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRApp(root)
    root.mainloop()
