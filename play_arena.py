import tkinter as tk

class PlayArena(tk.Frame):
        
    def __init__(self, parent, main_window):
        super().__init__(parent)

        self.main_window = main_window
        self.config = main_window.config

        self.grid(row=0, column=0)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)

        self.create_main_frame()

        self.frames = {}
        self.buttons = {}

        self.create_buttons()

        self.main_window.game.append_all_frames(self.main_window)

    def create_main_frame(self):
        self.main_frame= tk.Frame(self, bg=self.config.background, width=self.config.w_h, height=self.config.w_h)
        self.main_frame.pack()

    def create_buttons_frames(self):
        for row in range(self.config.row):
            self.frames[f"frame{row}"] = tk.Frame(self.main_frame, height=self.config.w_h)
            self.frames[f"frame{row}"].pack()
            self.main_window.game.append_all_frames(self.frames[f"frame{row}"])

    def create_buttons(self):
        self.create_buttons_frames()

        for row in range(self.config.row):
            for col in range(self.config.col):
                self.buttons[f"btn{row}_{col}"] = tk.Button(self.frames[f"frame{row}"], bg=self.config.background, fg=self.config.foreground, width=self.config.w_h//50, height=self.config.w_h//78, activebackground=self.config.foreground, activeforeground=self.config.background, bd=0)
                self.buttons[f"btn{row}_{col}"].configure(command=lambda current_row=row, current_col=col:self.main_window.game.player_guess(current_row, current_col))
                self.buttons[f"btn{row}_{col}"].pack(side="left")
                self.main_window.game.append_all_buttons(self.buttons[f"btn{row}_{col}"])
