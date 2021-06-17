import tkinter as tk

class MainMenu(tk.Frame):
        
    def __init__(self, parent, main_window):
        super().__init__(parent)

        self.main_window = main_window
        self.config = main_window.config

        self.grid(row=0, column=0)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)

        self.create_main_frame()
        self.create_title()
        self.create_opt_button()

        self.main_window.game.append_all_frames(self.main_frame)
        self.main_window.game.append_all_buttons(self.start_btn, self.settings_btn, self.statistic_btn, self.exit_btn)
        self.main_window.game.append_all_labels(self.title)
 
    def create_main_frame(self):
        self.main_frame= tk.Frame(self, bg=self.config.background, width=self.config.w_h, height=self.config.w_h)
        self.main_frame.pack()

    def create_title(self):
        self.title = tk.Label(self.main_frame, text="BattleShip", font=("Montserrat", 35), bg=self.config.background, fg=self.config.foreground)
        self.title.place(relx=.5, rely=.2, anchor="center")

    def create_opt_button(self):
        self.start_btn = tk.Button(self.main_frame, text="Start", font=("Montserrat", 20), width=10, bg=self.config.background, fg=self.config.foreground, activeforeground=self.config.background, activebackground=self.config.foreground, bd=0, highlightbackground=self.config.foreground, command=self.start)
        self.start_btn.place(relx=.5, rely=.5, anchor="center")

        self.settings_btn = tk.Button(self.main_frame, text="Settings", font=("Montserrat", 20), width=10, bg=self.config.background, fg=self.config.foreground, activeforeground=self.config.background, activebackground=self.config.foreground, bd=0, highlightbackground=self.config.foreground, command=lambda:self.main_window.change_page("settings_menu"))
        self.settings_btn.place(relx=.5, rely=.6, anchor="center")

        self.statistic_btn = tk.Button(self.main_frame, text="Statitics", font=("Montserrat", 20), width=10, bg=self.config.background, fg=self.config.foreground, activeforeground=self.config.background, activebackground=self.config.foreground, bd=0, highlightbackground=self.config.foreground, command=lambda:self.main_window.change_page("statistic_menu"))
        self.statistic_btn.place(relx=.5, rely=.7, anchor="center")

        self.exit_btn = tk.Button(self.main_frame, text="Exit", font=("Montserrat", 20), width=10, bg=self.config.background, fg=self.config.foreground, activeforeground=self.config.background, activebackground=self.config.foreground, bd=0, highlightbackground=self.config.foreground,  command=self.main_window.destroy)
        self.exit_btn.place(relx=.5, rely=.8, anchor="center")


    def start(self):
        self.main_window.change_page("play_arena")
        if self.config.row == 3:
            self.main_window.pages["main_menu"].title.configure(fg=self.config.background)
            self.main_window.pages["main_menu"].exit_btn.configure(fg=self.config.background, highlightbackground=self.config.background)
