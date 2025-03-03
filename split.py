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

        ctk.CTkLabel(self, text="Split a PDF in a single point", font=("Arial", 24, "bold")).pack(pady=20)

        button_frame=ctk.CTkFrame(self)
        button_frame.pack(pady=5)

        ctk.CTkButton(button_frame, text="Select a File", command=self.choose_file).grid(row=0,column=0,padx=5)
        self.splitPoint=ctk.CTkEntry(button_frame)
        self.splitPoint.grid(row=0,column=1,padx=5)
        ctk.CTkButton(button_frame, text="Split", command=self.split_file).grid(row=0,column=2, padx=5)
        

        

        ctk.CTkLabel(self, text="Split PDF's in multiple points", font=("Arial", 24, "bold")).pack(pady=20)

        button_frame2=ctk.CTkFrame(self)
        button_frame2.pack(pady=5)

        ctk.CTkButton(button_frame2, text="Select a File", command=self.choose_file).grid(row=0,column=0,padx=5)

        self.multiSplitPoints=ctk.CTkEntry(button_frame2)
        self.multiSplitPoints.grid(row=0,column=1,padx=5)
        ctk.CTkButton(button_frame2, text="Split", command=self.split_file_2).grid(row=0,column=2, padx=5)

        ctk.CTkButton(self, text="Back", command=lambda: controller.show_frame("MainMenu")).pack(pady=10)


        ctk.CTkButton(self, text="Exit", command=self.quit, fg_color="red",hover_color="white", corner_radius=12,width=100).pack(pady=5)

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

    def split_file_2(self):
        if not self.file_path:
            CTkMessagebox(message="No PDF selected!",icon="warning")
            return
        try:
            split_points=sorted(map(int, self.multiSplitPoints.get().split(',')))
        except ValueError:
            CTkMessagebox(message="Enter valid page numbers separated by commas!",icon="warning")
            return
        
        reader=PdfReader(self.file_path)
        total_pages=len(reader.pages)

        if any(p<=0 or p>= total_pages for p in split_points):
            CTkMessagebox(message="Invalid page number(s)!", icon="warning")
            return
        
        save_dir=filedialog.askdirectory(title="Select folder to save split PDFs")
        if not save_dir:
            return
        
        split_points=[0] + split_points+[total_pages]
        base_name=os.path.splitext(os.path.basename(self.file_path))[0]

        for i in range(len(split_points)-1):
            writer=PdfWriter()
            for j in range(split_points[i], split_points[i+1]):
                writer.add_page(reader.pages[j])
            output_path=os.path.join(save_dir, f"{base_name}_part{i+1}.pdf")
            with open(output_path, "wb") as output_file:
                writer.write(output_file)

        self.multiSplitPoints.delete(0,'end')
        CTkMessagebox(message="PDF successfully split at multiple points!", icon="check")