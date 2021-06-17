import tkinter as tk

class WinMenu(tk.Frame):
        
    def __init__(self, parent, main_window):
        super().__init__(parent)

        self.main_window = main_window
        self.config = main_window.config

        self.grid(row=0, column=0)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)

        self.create_main_frame()

        self.main_window.game.append_all_frames(self.main_frame)
        self.main_window.game.append_all_buttons(self.play_again_button, self.main_menu_button, self.exit_button)
        self.main_window.game.append_all_labels(self.title, self.coordinate)

    def create_main_frame(self):
        self.main_frame= tk.Frame(self, bg=self.config.background, width=self.config.w_h, height=self.config.w_h)
        self.main_frame.pack()

        self.create_title()
        self.create_coordinate()
        self.create_button()

    def create_title(self):
        self.title = tk.Label(self.main_frame, text="You Win!!!", font=("Montserrat", 35, "bold"), bg=self.config.background, fg=self.config.foreground)
        self.title.place(relx=.5, rely=.35, anchor="center")

    def create_coordinate(self):
        self.coordinate = tk.Label(self.main_frame, font=("Montserrat", 20), bg=self.config.background, fg=self.config.foreground)
        self.coordinate.place(relx=.5, rely=.45, anchor="center")

    def create_button(self):
        self.play_again_button = tk.Button(self.main_frame, text="Play Again", font=("Montserrat", 15), bg=self.config.background, fg=self.config.foreground, activebackground=self.config.foreground, bd=0, highlightbackground=self.config.foreground, activeforeground=self.config.background, command=self.play_again)
        self.play_again_button.place(relx=.38, rely=.55, anchor="center")

        self.main_menu_button = tk.Button(self.main_frame, text="Main Menu", font=("Montserrat", 15), bg=self.config.background, fg=self.config.foreground, activebackground=self.config.foreground, bd=0, highlightbackground=self.config.foreground, activeforeground=self.config.background, command=self.goto_main_menu)
        self.main_menu_button.place(relx=.62, rely=.55, anchor="center")

        self.exit_button = tk.Button(self.main_frame, text="Exit", font=("Montserrat", 15), width=8, bg=self.config.background, fg=self.config.foreground, activebackground=self.config.foreground, bd=0, highlightbackground=self.config.foreground, activeforeground=self.config.background, command=self.main_window.destroy)
        self.exit_button.place(relx=.5, rely=.65, anchor="center")

    def reset_play_arena(self):
        for row in range(self.config.row):
            for col in range(self.config.col):
                self.main_window.pages["play_arena"].buttons[f"btn{row}_{col}"].configure(text='', state="normal")

        self.main_window.game.correct_loc()

    def goto_main_menu(self):
        if self.config.row == 3:
            self.main_window.pages["main_menu"].title.configure(fg=self.config.foreground)
            self.main_window.pages["main_menu"].exit_btn.configure(fg=self.config.foreground, highlightbackground=self.config.foreground)
        self.reset_play_arena()
        self.main_window.change_page("main_menu")

    def play_again(self):
        self.reset_play_arena()
        self.main_window.change_page("play_arena")
