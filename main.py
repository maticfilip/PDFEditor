import customtkinter as ctk
import merge_option  # Import the merge window module

def open_merge_window():
    app.destroy()  # Close main window
    merge_option.run_merge_window()  # Open merge window

# Create Main Window
app = ctk.CTk()
app.geometry("600x400")
app.title("Main Menu")

btn_open_merge = ctk.CTkButton(app, text="Open Merge Window", command=open_merge_window)
btn_open_merge.pack(pady=20)

btn_exit = ctk.CTkButton(app, text="Exit", command=app.destroy)
btn_exit.pack(pady=20)

app.mainloop()
