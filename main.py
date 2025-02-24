from PyPDF2 import PdfMerger
import customtkinter as ctk
import os
from tkinter import filedialog
from PIL import Image
from CTkMessagebox import CTkMessagebox


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app=ctk.CTk()
app._state_before_windows_set_titlebar_color='zoomed'


btn_exit = ctk.CTkButton(app, text="Exit", command=app.destroy)
# btn_exit.pack(pady=10)
btn_exit.pack(side="bottom", anchor="e", pady=20, padx=20)


selected_files=[]

pdf_icon_path="pdf-40.png"
pdf_icon=ctk.CTkImage(light_image=Image.open(pdf_icon_path), size=(50,50))

file_frame=ctk.CTkScrollableFrame(app, width=600, height=200)
file_frame.pack(pady=10, padx=20, fill="both", expand=True)

def choose_file():
    global selected_files
    filetypes=[('PDF','*.pdf')]
    paths=filedialog.askopenfilenames(title="Choose file",filetypes=filetypes)

    if paths:
        selected_files=list(paths)
        update_file_display() 

def update_file_display():
    for widget in file_frame.winfo_children():
        widget.destroy()

    if selected_files:
        columns=3
        for index, file in enumerate(selected_files):
            file_name=os.path.basename(file)

            card=ctk.CTkFrame(file_frame, corner_radius=10, width=150, height=180)
            card.grid(row=index // columns, column=index % columns, padx=10, pady=10)

            icon_label=ctk.CTkLabel(card, image=pdf_icon, text="")
            icon_label.pack(pady=10)

            file_label=ctk.CTkLabel(card, text=file_name, font=("Arial",12), text_color="black", wraplength=140)
            file_label.pack(pady=5)

def merge_files():
    global selected_files

    merger=PdfMerger()
    if len(selected_files)<=1:
        CTkMessagebox(message="Not enough documents were selected!", icon="warning", option_1="Cancel")
        return
    
    save_path=filedialog.asksaveasfilename(
        title="Save Merged PDF:",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        )

    if not save_path:
        return
    
    # save_path=os.path.join(save_dir, "merged.pdf")
    for pdf in selected_files:
        merger.append(pdf)
    
    merger.write(save_path)
    merger.close

    selected_files.clear()

    for widget in file_frame.winfo_children():
        widget.destroy()

    CTkMessagebox(message="The file has been successfully merged!", icon="check", option_1="Thanks", master=app)


btn_select=ctk.CTkButton(app, text="Select Files", command=choose_file)
btn_select.pack(pady=5)
btn_select.place(x=20, y=20)  # Top left corner

btn_merge=ctk.CTkButton(app, text="Merge Selecter", command=merge_files)
btn_merge.pack(pady=5)



app.mainloop()