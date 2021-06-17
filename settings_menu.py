import tkinter as tk

class SettingsMenu(tk.Frame):
        
    def __init__(self, parent, main_window):
        super().__init__(parent)

        self.main_window = main_window
        self.config = main_window.config

        self.grid(row=0, column=0)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)

        self.create_main_frame()
        self.create_content()
        self.is_enabled()

        self.main_window.game.append_all_frames(self.main_frame, self.theme_config_subframe)
        self.main_window.game.append_all_buttons(self.back_button)
        self.main_window.game.append_all_labels(self.theme_config_label)

    def create_main_frame(self):
        self.main_frame= tk.Frame(self, bg=self.config.background, width=self.config.w_h, height=self.config.w_h)
        self.main_frame.pack()

    def create_content(self):
        self.back_button = tk.Button(self.main_frame, text="Back", font=("Montserrat", 15), bg=self.config.background, fg=self.config.foreground, activebackground=self.config.foreground, activeforeground=self.config.background, bd=0, command=lambda:self.main_window.change_page("main_menu"))
        self.back_button.place(relx=0, rely=0)

        self.theme_config_label = tk.Label(self.main_frame, text="Theme", font=("Montserrat", 30), bg=self.config.background, fg=self.config.foreground)
        self.theme_config_label.place(relx=0.15, rely=0.1)

        self.theme_config_subframe = tk.Frame(self.main_frame, width=self.config.w_h//4, height=self.config.w_h//12, bg=self.config.background)
        self.theme_config_subframe.place(relx=0.62, rely=0.1)

        self.light_theme_config_button = tk.Button(self.theme_config_subframe, font=("Montserrat", 30), width=2, bg="white", fg="black", activebackground="white", activeforeground="black", highlightbackground="black", bd=0, command=lambda color="light":self.main_window.change_theme(self.light_theme_config_button, self.dark_theme_config_button, color))
        self.light_theme_config_button.grid(row=0, column=0, padx=10)

        self.dark_theme_config_button = tk.Button(self.theme_config_subframe, font=("Montserrat", 30), width=2, bg="black", fg="white", activebackground="black", activeforeground="white", bd=0, command=lambda color="dark":self.main_window.change_theme(self.dark_theme_config_button, self.light_theme_config_button, color))
        self.dark_theme_config_button.grid(row=0, column=1, padx=10)

    def is_enabled(self):
        current_theme = self.config.data["theme"]
        if current_theme == "light":
            self.light_theme_config_button.configure(text="✓")
        elif current_theme == "dark":
            self.dark_theme_config_button.configure(text="✓")
