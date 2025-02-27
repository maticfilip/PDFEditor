import customtkinter as ctk
from PyPDF2 import PdfMerger
from tkinter import filedialog
from CTkMessagebox import CTkMessagebox
from PIL import Image
import os

class MergeFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.selected_files = []
        self.pdf_icon_path="pdf-40.png"
        self.pdf_icon=ctk.CTkImage(light_image=Image.open(self.pdf_icon_path), size=(50,50))

        ctk.CTkLabel(self, text="Merge PDFs", font=("Arial", 24, "bold")).pack(pady=20)

        self.file_frame = ctk.CTkScrollableFrame(self, width=600, height=200)
        self.file_frame.pack(pady=10, padx=20, fill="both", expand=True)


        button_frame=ctk.CTkFrame(self)
        button_frame.pack(pady=5)

        ctk.CTkButton(button_frame, text="Select Files", command=self.choose_file).grid(row=0,column=0,padx=5)
        ctk.CTkButton(button_frame, text="Merge PDFs", command=self.merge_files).grid(row=0,column=1,padx=5)
        ctk.CTkButton(button_frame, text="Back", command=lambda: controller.show_frame("MainMenu")).grid(row=0,column=2,padx=5)

        ctk.CTkButton(self, text="Exit", command=self.quit, fg_color="red",hover_color="white", corner_radius=12,width=100).pack(pady=10)


        self.update_idletasks()
        controller.geometry(f"{self.winfo_reqwidth()}x{self.winfo_reqheight()}")

    def choose_file(self):
        paths = filedialog.askopenfilenames(filetypes=[('PDF', '*.pdf')])
        if paths:
            self.selected_files = list(paths)
            self.update_file_display()

    def update_file_display(self):
        for widget in self.file_frame.winfo_children():
            widget.destroy()

        if self.selected_files:
            columns = 3
            for index, file in enumerate(self.selected_files):
                file_name = os.path.basename(file)

                # Create a new card for each file (avoid overwriting)
                card = ctk.CTkFrame(self.file_frame, corner_radius=10, width=150, height=180)
                card.grid(row=index // columns, column=index % columns, padx=10, pady=10)

                # Icon Label
                icon_label = ctk.CTkLabel(card, image=self.pdf_icon, text="")  # Display PDF icon
                icon_label.pack(pady=5)

                # File Name Label
                file_label = ctk.CTkLabel(card, text=file_name, font=("Arial", 12), text_color="gray", wraplength=140)
                file_label.pack(pady=5)


        for file in self.selected_files:
            self.file_label=ctk.CtkLabel(self.card, text=file_name, font=("Arial",12), text_color="gray",wraplength=140 )
            self.file_label.pack(pady=5)

    def merge_files(self):
        if len(self.selected_files) <= 1:
            CTkMessagebox(message="Not enough documents selected!", icon="warning")
            return

        save_path = filedialog.asksaveasfilename(
            title="Save Merged PDF:",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )

        if not save_path:
            return
        
        if save_path:
            merger = PdfMerger()
            for pdf in self.selected_files:
                merger.append(pdf)
            merger.write(save_path)
            merger.close()
            CTkMessagebox(message="PDFs merged successfully!", icon="check")
