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

        # Theme
        self.dark_mode = False
        self.fg_color = "black"
        self.bg_color = "white"

        # UI
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

        self.theme_btn = tk.Button(root, text="Switch to Dark Mode", command=self.toggle_theme)
        self.theme_btn.pack(pady=15)

        self.apply_theme()

    def generate_qr(self):
        data = self.entry.get().strip()
        if not data:
            messagebox.showwarning("Input Required", "Please enter some text or a URL.")
            return

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=self.fg_color, back_color=self.bg_color)

        self.qr_img = img
        img_resized = img.resize((250, 250))
        self.tk_img = ImageTk.PhotoImage(img_resized)
        self.qr_label.config(image=self.tk_img)

        self.entry.delete(0, tk.END)
        messagebox.showinfo("Success", "QR Code generated!")

    def save_qr(self):
        if not hasattr(self, 'qr_img'):
            messagebox.showwarning("No QR Code", "Please generate a QR Code first.")
            return

        file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file:
            self.qr_img.save(file)
            messagebox.showinfo("Saved", f"QR Code saved at:\n{file}")

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def apply_theme(self):
        if self.dark_mode:
            self.root.configure(bg="#2E2E2E")
            self.label.config(bg="#2E2E2E", fg="white")
            self.entry.config(bg="#3C3C3C", fg="white", insertbackground="white")
            self.theme_btn.config(text="Switch to Light Mode", bg="#444", fg="white")
        else:
            self.root.configure(bg="white")
            self.label.config(bg="white", fg="black")
            self.entry.config(bg="white", fg="black", insertbackground="black")
            self.theme_btn.config(text="Switch to Dark Mode", bg="SystemButtonFace", fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRApp(root)
    root.mainloop()
