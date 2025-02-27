import customtkinter as ctk
from PyPDF2 import PdfReader, PdfWriter
from tkinter import filedialog
from CTkMessagebox import CTkMessagebox
import os
from hurry.filesize import size

class ResizeFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.selected_file = None

        ctk.CTkLabel(self, text="Resize PDF", font=("Arial", 24, "bold")).pack(pady=20)

        self.file_label = ctk.CTkLabel(self, text="No file selected")
        self.file_label.pack(pady=5)

        ctk.CTkButton(self, text="Choose PDF", command=self.choose_file).pack(pady=5)
        ctk.CTkButton(self, text="Compress PDF", command=self.compress_pdf).pack(pady=5)
        ctk.CTkButton(self, text="Back", command=lambda: controller.show_frame("MainMenu")).pack(pady=5)

        ctk.CTkButton(self, text="Exit", command=self.quit, fg_color="red",hover_color="white", corner_radius=12,width=100).pack(pady=10)

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[('PDF', '*.pdf')])
        if file_path:
            self.selected_file = file_path
            self.file_label.configure(text=os.path.basename(file_path))

    def compress_pdf(self):
        if not self.selected_file:
            CTkMessagebox(message="No PDF selected!", icon="warning")
            return

        reader = PdfReader(self.selected_file)
        writer = PdfWriter()
        original_size = size(os.path.getsize(self.selected_file))

        for page in reader.pages:
            page.compress_content_streams()
            writer.add_page(page)

        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if save_path:
            with open(save_path, "wb") as f:
                writer.write(f)

            compressed_size = size(os.path.getsize(save_path))
            CTkMessagebox(message=f"Old PDF: {original_size}, New PDF: {compressed_size}", icon="check")
