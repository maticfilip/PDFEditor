import customtkinter as ctk

class MainMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ctk.CTkLabel(self, text="PDF Editor", font=("Arial", 24, "bold")).pack(pady=20)

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

        ctk.CTkButton(self, text="Exit", command=self.quit, fg_color="red",hover_color="white", corner_radius=12,width=100).pack(pady=10)
