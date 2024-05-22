class CricketMatch:
    def start_game(self):
        self.total_runs = 0
        self.wickets = 0
        self.ball = 0
        self.over = 0
        self.player_a_runs = 0
        self.player_b_runs = 0
        self.player_a_ball = 0
        self.player_b_ball = 0
        self.star_a = ""
        self.star_b = ""
        self.players_name = []
        self.add_players_name()
        self.player_a = self.players_name[0]
        self.player_b = self.players_name[1]
        self.batsman = self.player_a
        self.bollers_name = []

    def add_bollers(self):
        baller = input("Enter Boller Name: ")
        if baller not in self.bollers_name:
            self.bollers_name.append(baller)
        else:
            print(f"{baller} is already in the list of bowlers.")

    def add_players_name(self):
        for i in range(1, 6):
            player = input(f'Enter player {i} name: ')
            self.players_name.append(player)

    def overs_in_match(self):
        while self.over < 2 and self.wickets < 4:
            self.add_bollers()
            self.ball_in_over()
            self.over += 1
            self.over_change_player()
        self.game_over()

    def ball_in_over(self):
        self.ball = 0
        while self.ball < 6 and self.wickets < 4:
            self.print_score()
            self.ball += 1
            self.score_off_balls()

    def score_off_balls(self):
        score = input('Score (0-6 or W for wicket): ')
        if score.isdigit():
            score = int(score)
            if score in (0, 1, 2, 3, 4, 6):
                runs = score
                self.total_runs += runs
                self.player_runs(score)
                self.player_change(score)
            else:
                print("Invalid score, please enter a valid number (0-6).")
        elif score.lower() == "w":
            self.wickets += 1
            if self.wickets < 4:
                self.player_change_wickets()
        else:
            print("Invalid input, please enter a valid number (0-6) or 'W' for wicket.")

    def print_score(self):
        self.star_mark()
        print(f'Total {self.total_runs}/{self.wickets} over: {self.over}.{self.ball}  '
              f'{self.player_a} - {self.player_a_runs} ({self.player_a_ball}) {self.star_a} / '
              f'{self.player_b} - {self.player_b_runs} ({self.player_b_ball}) {self.star_b}')

    def game_over(self):
        if self.wickets == 4:
            if self.ball == 6:
                self.ball = 0
            else:
                self.over -= 1
        elif self.over == 2:
            self.ball = 0
        self.print_score()
        print("Game Over")

    def player_change(self, score):
        if score in (1, 3):
            if self.batsman == self.player_a:
                self.batsman = self.player_b
            else:
                self.batsman = self.player_a

    def player_runs(self, score):
        if self.batsman == self.player_a:
            self.player_a_runs += score
            self.player_a_ball += 1
        else:
            self.player_b_runs += score
            self.player_b_ball += 1
        self.star_mark()

    def player_change_wickets(self):
        if self.batsman == self.player_a:
            print(f'{self.player_a} is out! Runs: {self.player_a_runs}, Balls: {self.player_a_ball}')
            if self.wickets + 1 < len(self.players_name):
                self.player_a = self.players_name[self.wickets + 1]
                self.player_a_runs = 0
                self.player_a_ball = 0
                self.batsman = self.player_a
        else:
            print(f'{self.player_b} is out! Runs: {self.player_b_runs}, Balls: {self.player_b_ball}')
            if self.wickets + 1 < len(self.players_name):
                self.player_b = self.players_name[self.wickets + 1]
                self.player_b_runs = 0
                self.player_b_ball = 0
                self.batsman = self.player_b

    def over_change_player(self):
        if self.batsman == self.player_a:
            self.batsman = self.player_b
        else:
            self.batsman = self.player_a

    def star_mark(self):
        if self.batsman == self.player_a:
            self.star_a = "*"
            self.star_b = ""
        else:
            self.star_b = "*"
            self.star_a = ""

def main():
    first_innings = CricketMatch()
    second_innings = CricketMatch()
    first_innings.start_game()
    first_innings.overs_in_match()
    second_innings.start_game()
    second_innings.overs_in_match()

if __name__ == "__main__":
    main()
