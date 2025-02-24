import customtkinter as ctk
import merge_option  # Import the merge window module
import resize_option
from tkinter import font as tkFont



def open_merge_window():
    app.destroy()  # Close main window
    merge_option.run_merge_window()  
    
def open_resize_window():
    app.destroy()
    resize_option.run_resize_window()


app = ctk.CTk()
app.geometry("600x400")
app.title("Main Menu")

custom_font_path="fonts/Roboto-Regular.ttf"
custom_font_name="RobotoRegular"
tkFont.Font(family=custom_font_name, size=24)

header_label=ctk.CTkLabel(app, text="PDF EDITOR", font=("RobotoRegular", 24, "bold"), text_color="#0285ff")
header_label.pack(pady=20)

btn_open_merge = ctk.CTkButton(app, 
            text="Merge PDF files", #Text to be displayed
            fg_color="#0285ff", #color of the button
            hover_color="white", #color of the button when mouse is over
            font=("RobotoRegular", 16), #font used
            corner_radius=12,
            width=100, 
            command=open_merge_window)
btn_open_merge.pack(pady=20)

btn_open_resize=ctk.CTkButton(app, 
            text="Resize a PDF file", #Text to be displayed
            fg_color="#0285ff", #color of the button
            hover_color="white", #color of the button when mouse is over
            font=("RobotoRegular", 16), #font used
            corner_radius=12,
            width=100, 
            command=open_resize_window)
btn_open_resize.pack(pady=20)


btn_exit = ctk.CTkButton(app, text="Exit", command=app.destroy)
btn_exit.pack(pady=20)

app.mainloop()
