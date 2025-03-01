import customtkinter as ctk
import tkinter as tk

class MainMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ctk.CTkLabel(self, text="PDF Editor", font=("Arial", 24, "bold")).pack(pady=20)

        self.tooltip_window=None

        btn_merge = ctk.CTkButton(
            self, text="Merge PDFs",
            command=lambda: controller.show_frame("MergeFrame"),
            fg_color="#0285ff", hover_color="white",
            corner_radius=12, width=100
        )
        btn_merge.pack(pady=5)

        btn_resize = ctk.CTkButton(
            self, text="Resize PDFs",
            command=lambda: controller.show_frame("ResizeFrame"),
            fg_color="#0285ff", hover_color="white",
            corner_radius=12, width=100
        )
        btn_resize.pack(pady=5)

        btn_split = ctk.CTkButton(
            self, text="Split a PDF",
            command=lambda: controller.show_frame("SplitFrame"),
            fg_color="#0285ff", hover_color="white",
            corner_radius=12, width=100
        )
        btn_split.pack(pady=5)

        # Bind hover events to show/hide tooltip
        btn_split.bind("<Enter>", lambda event: self.show_tooltip(event, "Split a PDF into multiple files at chosen pages, or at just one page."))
        btn_split.bind("<Leave>", self.hide_tooltip)

        btn_merge.bind("<Enter>", lambda event:self.show_tooltip(event, "Merge multiple PDF files into one."))
        btn_merge.bind("<Leave>",self.hide_tooltip)

        btn_resize.bind("<Enter>", lambda event:self.show_tooltip(event, "Compress your PDF file to minimize memory usage."))
        btn_resize.bind("<Leave>",self.hide_tooltip)

        ctk.CTkButton(self, text="Exit", command=self.quit, fg_color="red", hover_color="white", corner_radius=12, width=100).pack(pady=10)

    def show_tooltip(self, event, text):
        """Create a Toplevel tooltip that floats above all widgets"""
        if self.tooltip_window:
            self.tooltip_window.destroy()  # Remove old tooltip if it exists

        self.tooltip_window = tk.Toplevel(self)
        self.tooltip_window.wm_overrideredirect(True)  # Remove window border
        self.tooltip_window.configure(bg="gray")  # Background color

        label = tk.Label(self.tooltip_window, text=text, font=("Arial", 12), bg="gray", fg="white", wraplength=200, padx=5, pady=3)
        label.pack()

        x = event.widget.winfo_rootx() + 20  # Offset tooltip slightly
        y = event.widget.winfo_rooty() + 30

        window_width = self.winfo_toplevel().winfo_width()
        window_height = self.winfo_toplevel().winfo_height()

        if x + 220 > window_width:  
            x = window_width - 220  
        if y + 50 > window_height:  
            y -= 40  

        self.tooltip_window.wm_geometry(f"+{x}+{y}")  

    def hide_tooltip(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None