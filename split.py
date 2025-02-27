import customtkinter as ctk
from PyPDF2 import PdfReader, PdfWriter
from tkinter import filedialog
from CTkMessagebox import CTkMessagebox
from PIL import Image
import os

class SplitFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller=controller

        ctk.CTkLabel(self, text="Split a PDF", font=("Arial", 24, "bold")).pack(pady=20)

        button_frame=ctk.CTkFrame(self)
        button_frame.pack(pady=5)

        ctk.CTkButton(button_frame, text="Select a File", command=self.choose_file).grid(row=0,column=0,padx=5)
        self.splitPoint=ctk.CTkEntry(button_frame)
        self.splitPoint.grid(row=0,column=1,padx=5)
        ctk.CTkButton(button_frame, text="Split", command=self.split_file).grid(row=0,column=2, padx=5)
        ctk.CTkButton(button_frame, text="Back", command=lambda: controller.show_frame("MainMenu")).grid(row=0,column=3,padx=5)

        ctk.CTkButton(self, text="Exit", command=self.quit, fg_color="red",hover_color="white", corner_radius=12,width=100).pack(pady=10)

    def choose_file(self):
        self.file_path = filedialog.askopenfilename(title="Choose file", filetypes=[("PDF", "*.pdf")])
    def split_file(self):
        if not self.file_path:
            CTkMessagebox(message="No PDF selected!",icon="warning")
            return
        try:
            split_at=int(self.splitPoint.get())
        except ValueError:
            CTkMessagebox(message="Enter a valid page number!", icon="warning")
            return
        
        reader=PdfReader(self.file_path)
        total_pages=len(reader.pages)

        if split_at<=0 or split_at>=total_pages:
            CTkMessagebox(message="Invalid page number!", icon="warning")
            return
        
        save_dir=filedialog.askdirectory(title="Select folder to save split PDFs")
        if not save_dir:
            return
        
        writer1, writer2=PdfWriter(),PdfWriter()

        for i in range(total_pages):
            if i<split_at:
                writer1.add_page(reader.pages[i])
            else:
                writer2.add_page(reader.pages[i])
            
        base_name=os.path.splitext(os.path.basename(self.file_path))[0]

        part1_path = os.path.join(save_dir, f"{base_name}_part1.pdf")
        part2_path = os.path.join(save_dir, f"{base_name}_part2.pdf")

        with open(part1_path, "wb") as f1:
            writer1.write(f1)
        with open(part2_path, "wb") as f2:
            writer2.write(f2)

        CTkMessagebox(message="PDF successfully split!", icon="check")