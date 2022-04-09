class Stats():
    # Статистка

    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open('high-score.txt','r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        # Статистика яка міняється під час ігри
        self.guns_left = 3
        self.score = 0
