"""
Nama : Dheovan Winata Alvian
Kelas: 10 Komputer 1
"""

import tkinter as tk
from random import randint
import os

from config import Config
from main_menu import MainMenu
from settings_menu import SettingsMenu
from play_arena import PlayArena
from win_menu import WinMenu
from statistic_menu import StatisticMenu

class MainWindow(tk.Tk):
        
    def __init__(self, Game):
        super().__init__()

        self.game = Game
        self.config = self.game.config

        self.title(self.config.title)
        self.geometry(self.config.screen_size)

        self.create_container()

        self.create_pages()

    def create_container(self):
        self.container = tk.Frame(self, bg=self.config.background)
        self.container.pack(fill="both", expand=True)

    def create_pages(self):
        self.pages = {}
        self.pages["win_menu"] = WinMenu(self.container, self)
        self.pages["play_arena"] = PlayArena(self.container, self)
        self.pages["statistic_menu"] = StatisticMenu(self.container, self)
        self.pages["settings_menu"] = SettingsMenu(self.container, self)
        self.pages["main_menu"] = MainMenu(self.container, self)

    def change_page(self, page):
        raised_page = self.pages[page]
        raised_page.tkraise()

    def change_theme(self, current_button=None, another_button=None, theme_name="light"):
        if theme_name == "dark":
            for group in self.config.all_frames:
                for frame in group:
                    frame.configure(bg="#000")
            for group in self.config.all_buttons:
                for button in group:
                    button.configure(bg="#000", fg="#FAFAFA", activebackground="#FAFAFA", activeforeground="#000", highlightbackground="#FAFAFA")
            for group in self.config.all_labels:
                for label in group:
                    label.configure(bg="#000", fg="#FAFAFA")
        elif theme_name == "light":
            for group in self.config.all_frames:
                for frame in group:
                    frame.configure(bg="#FAFAFA")
            for group in self.config.all_buttons:
                for button in group:
                    button.configure(bg="#FAFAFA", fg="#000", activebackground="#000", activeforeground="#FAFAFA", highlightbackground="#FAFAFA")
            for group in self.config.all_labels:
                for label in group:
                    label.configure(bg="#FAFAFA", fg="#000")
        save_theme_name = {
                "theme" : theme_name,
                "row" : 5,
                "col" : 5
                }
        self.config.save_data(save_theme_name)
        if current_button:
            current_button.configure(text='✓')
            another_button.configure(text='')
        self.destroy()
        os.system("python3 main.py")

class Game:
        
    def __init__(self):
        self.config = Config()
        self.main_window = MainWindow(self)

        self.correct_loc()

    def correct_loc(self):
        self.correct_row = randint(0, self.config.row-1)
        self.correct_col = randint(0, self.config.col-1)
        # print(self.correct_row, self.correct_col) # only for debugging

    def player_guess(self, row, col):
        if (row == self.correct_col) and (col == self.correct_row):
            # Add coordinate position
            self.main_window.change_page("win_menu")
            self.main_window.pages["win_menu"].coordinate.configure(text=f"Correct Location: ({self.correct_row+1}, {self.correct_col+1})")
            # Statistic thing (win value)
            self.config.win += 1
            self.main_window.pages["statistic_menu"].win_value.configure(text=self.config.win)
            # Probability statistic
            self.config.win_rate_history.append(self.config.default_value)
            self.config.calculate_win_rates()
            self.main_window.pages["statistic_menu"].win_rate_value.configure(text="%.f%%" % (self.config.current_win_rate))
            self.config.default_value = 100
            statistic = {
                    "win" : self.config.win,
                    "wrong" : self.config.wrong,
                    "win_rate" : self.config.current_win_rate,
                    "win_rate_history" : self.config.win_rate_history
                    }
            self.config.save_statistic_data(statistic)
        else:
            # Change button text
            self.main_window.pages["play_arena"].buttons[f"btn{row}_{col}"].configure(text="X", font=("Arial", 11, "bold"), state="disabled")
            # Statistic thing (wrong value)
            self.config.wrong += 1
            self.main_window.pages["statistic_menu"].wrong_value.configure(text=self.config.wrong)
            # Probability statistic
            self.config.default_value -= self.config.one_block_value
        # print(self.config.default_value) # current win rate

    def append_all_frames(self, *frames):
        self.config.all_frames.append(frames)

    def append_all_buttons(self, *buttons):
        self.config.all_buttons.append(buttons)

    def append_all_labels(self, *labels):
        self.config.all_labels.append(labels)

    def run(self):
        self.main_window.mainloop()

if __name__ == "__main__":
    battleship = Game()
    battleship.run()
