import tkinter as tk

class StatisticMenu(tk.Frame):
        
    def __init__(self, parent, main_window):
        super().__init__(parent)

        self.main_window = main_window
        self.config = main_window.config

        self.grid(row=0, column=0)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)

        self.create_main_frame()
        self.create_content()

        self.main_window.game.append_all_frames(self.main_frame)
        self.main_window.game.append_all_buttons(self.back_button)
        self.main_window.game.append_all_labels(self.win_label, self.win_value, self.wrong_label, self.wrong_value)

    def create_main_frame(self):
        self.main_frame= tk.Frame(self, bg=self.config.background, width=self.config.w_h, height=self.config.w_h)
        self.main_frame.pack()

    def create_content(self):
        win = self.config.win
        wrong = self.config.wrong
        self.back_button = tk.Button(self.main_frame, text="Back", font=("Montserrat", 15), bg=self.config.background, fg=self.config.foreground, activebackground=self.config.foreground, activeforeground=self.config.background, bd=0, command=lambda:self.main_window.change_page("main_menu"))
        self.back_button.place(relx=0, rely=0)

        self.win_label = tk.Label(self.main_frame, text="Win", font=("Montserrat", 30), bg=self.config.background, fg=self.config.foreground)
        self.win_label.place(relx=0.15, rely=0.1)

        self.win_value = tk.Label(self.main_frame, text=win, font=("Montserrat", 30), bg=self.config.background, fg=self.config.foreground)
        self.win_value.place(relx=0.70, rely=0.1)

        self.wrong_label = tk.Label(self.main_frame, text="Wrong", font=("Montserrat", 30), bg=self.config.background, fg=self.config.foreground)
        self.wrong_label.place(relx=0.15, rely=0.2)

        self.wrong_value = tk.Label(self.main_frame, text=wrong, font=("Montserrat", 30), bg=self.config.background, fg=self.config.foreground)
        self.wrong_value.place(relx=0.70, rely=0.2)

        self.win_rate_label = tk.Label(self.main_frame, text="Win Rate", font=("Montserrat", 30), bg=self.config.background, fg=self.config.foreground)
        self.win_rate_label.place(relx=0.15, rely=0.3)

        self.win_rate_value = tk.Label(self.main_frame, text="%.f%%" % (self.config.current_value), font=("Montserrat", 30), bg=self.config.background, fg=self.config.foreground)
        self.win_rate_value.place(relx=0.70, rely=0.3)
