def start_game():
    global total_runs, wickets, ball, over, batsmen, player_a, player_b, player_a_runs, player_b_runs
    total_runs = 0
    wickets = 0
    ball = 0
    over = 0
    player_a = "shehan"
    player_b = "hasaranga"
    player_a_runs = 0
    player_b_runs = 0
    batsmen = player_a

def overs_in_match():
    global over, ball
    while over < 2 and wickets < 4:
        ball_in_over()  # passing argument
        over += 1
    game_over()

def ball_in_over():
    global ball
    ball = 0
    while ball < 6 and wickets < 4:
        print_score()
        ball += 1
        score_off_balls()

def score_off_balls():
    global total_runs, wickets
    score = input('Score: ')
    if score.isdigit():  # validation
        score = int(score)
        if score in (0, 1, 2, 3, 4, 6):
            runs = score
            total_runs += runs
            player_runs(runs)
            player_change(score)
    elif score.lower() == "w":
        wickets += 1
        player_change_wickets()

def print_score():
    print(f'Total {total_runs}/{wickets} over: {over}.{ball}')

def game_over():
    global over, ball
    if wickets == 4:
        if ball == 6:
            ball = 0
        else:
            over -= 1
    elif over == 2:
        ball = 0
    print_score()
    print("Game Over")

def player_change(score):
    global batsmen, player_a, player_b
    if score in (1, 3):
        if batsmen == player_a:
            batsmen = player_b
        else:
            batsmen = player_a

def player_runs(score):
    global batsmen, player_a_runs, player_b_runs
    if batsmen == player_a:
        player_a_runs += score
    else:
        player_b_runs += score

def player_change_wickets():
    global batsmen, player_a, player_b, player_a_runs, player_b_runs
    if batsmen == player_a:
        print(f'{player_a} Runs={player_a_runs}')
        new_player = input("Enter new player: ")
        player_a_runs = 0
        player_a = new_player
        batsmen = player_a
        print(player_a)
    else:
        print(f'{player_b} Runs={player_b_runs}')
        new_player = input("Enter new player: ")
        player_b_runs = 0
        player_b = new_player
        batsmen = player_b

start_game()
overs_in_match()
