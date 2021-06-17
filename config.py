from json import load, dump

class Config:
        
    def __init__(self):
        self.title = "Battleship"

        # Screen Size
        base = 7
        self.w_h = base*100  # width and height
        self.screen_size = f"{self.w_h}x{self.w_h}+600+200"


        # JSON
        self.path = "json/config.json"
        self.statistic_path = "json/statistic.json"
        self.load_data()
        self.load_statistic_data()

        # Color
        if self.data["theme"] == "light":
            self.background = "#FAFAFA"
            self.foreground = "#000000"
        elif self.data["theme"] == "dark":
            self.background = "#000000"
            self.foreground = "#FAFAFA"

        # Board : min = 3, max = 5
        self.row = self.data["row"]
        self.col = self.data["col"]

        # All element's lists
        # In order to change the theme, we have to append all elements in every pages and configure it using a for loop
        self.all_buttons = []
        self.all_labels = []
        self.all_frames = []

        # statistic
        self.win = int(self.statistic_data["win"])
        self.wrong = int(self.statistic_data["wrong"])

        ## statistic value (winning probability / win rate)
        self.one_block_value = 1/(self.row*self.col) * 100 # This mean like a value per block of the row*col (example: the value of 1/16 = 6.25% so if we do 6.25$ it will be 100%)
        self.default_value = 100  # 100%
        self.current_value = self.statistic_data["win_rate"]
        self.win_rate_history = self.statistic_data["win_rate_history"]
        self.calculate_win_rates()

    def load_data(self):
        with open(self.path, 'r') as file:
            self.data = load(file)

    def save_data(self, value):
        with open(self.path, 'w') as file:
            dump(value, file, indent=2)

    def load_statistic_data(self):
        with open(self.statistic_path, 'r') as file:
            self.statistic_data = load(file)

    def save_statistic_data(self, value):
        with open(self.statistic_path, 'w') as file:
            dump(value, file, indent=2)

    def calculate_win_rates(self):
        length_rates = len(self.win_rate_history)
        calculated_value = 0
        if length_rates == 0:
            length_rates += 1
        for win_rate in self.win_rate_history:
            calculated_value += win_rate
        calculated_value /= length_rates
        self.current_win_rate = calculated_value
