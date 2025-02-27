from PyPDF2 import PdfReader, PdfWriter
import customtkinter as ctk
import os
from tkinter import filedialog
from PIL import Image
from CTkMessagebox import CTkMessagebox
from hurry.filesize import size

def run_resize_window():
    app=ctk.CTk()
    app._state_before_windows_set_titlebar_color='zoomed'
    app.title("Resize a PDF")

    compressed_file=None

    selected_file=ctk.StringVar()

    def choose_file():
        filetypes=[('PDF','*.pdf')]
        path=filedialog.askopenfilename(title="Choose file", filetypes=filetypes)
        if path:
            selected_file.set(path)
    
    def compress_pdf():
        global compressed_file
        file_path=selected_file.get()

        if not file_path:
            CTkMessagebox(message="No PDF selected!",icon="warning")
            return

        reader=PdfReader(file_path)
        writer=PdfWriter()

        sizeOf=size(os.path.getsize(file_path))
        
        for page in reader.pages:
            page.compress_content_streams()
            writer.add_page(page)

        save_path=filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if save_path:
            with open(save_path, "wb") as f:
                writer.write(f)
            sizeOf2=size(os.path.getsize(save_path))
            CTkMessagebox(message="Old PDF size was {0}, and now it's {1}".format(sizeOf,sizeOf2), icon="check", master=app, option_1="Thanks")

    title_label=ctk.CTkLabel(app,text="Compress PDF", font=("Arial", 24, "bold"))
    title_label.pack(pady=20)

    file_btn=ctk.CTkButton(app, text="Choose PDF", command=choose_file)
    file_btn.pack(pady=10)

    file_label=ctk.CTkLabel(app, textvariable=selected_file, wraplength=400)
    file_label.pack(pady=5)

    compress_btn=ctk.CTkButton(app, text="Compress PDF", command=compress_pdf)
    compress_btn.pack(pady=20)

    app.mainloop()

            
