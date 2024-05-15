def cricket_game():
    total = 0
    over = 0
    out = 0
    ball = 1
    player_A = "shehan"
    player_B = "hasaranga"
    player_A_runs = 0
    player_B_runs = 0
    batsman = player_A
    total_run = 0
    over_in_match(over,out)

def runs(over,ball,out,total_run,player_change):
    print(over, ".", ball)
    mark = input("ball mark=")
    if mark == "out":
        out = out + 1
        if out <= 3:
            play_change_wickets(mark)
        else:
            return


    else:
        total_run = total_run + int(mark)
        batsman_run()
        player_change()
def ball_in_match(ball):
    while (7 > ball):
        runs()
    ball += 1

def over_in_match(over,out):
    while (over < 7):
        ball_in_match()
    over = over + 1
    if out == 3:
        print(out)
        return

def player_run_change(batsman,player_A,player_B,mark,player_A_runs,player_B_runs,total_run):
    if int(mark) == 1 or int(mark) == 3:
        if batsman == player_A:
            batsman = player_B
        else:
            batsman = player_A
    print(batsman)
    print(player_A, "-",player_A_runs)
    print(player_B, "-",player_B_runs)
    print("total runs -",total_run)

def batsman_run(batsman,player_A,player_A_runs,mark,player_B_runs):
    if batsman == player_A:
        player_A_runs = player_A_runs + int(mark)

    else:
        player_B_runs = player_B_runs + int(mark)

def play_change_wickets(batsman,player_A,player_A_runs,player_B,player_B_runs):
    if batsman == player_A:
        print(f'{player_A} runs ={player_A_runs}')
        new_player = input("Enter new player")
        player_A = new_player
        player_A_runs = 0
        batsman = player_A
        print(player_A)
    else:
        print(f'{player_B} runs={player_B_runs}')
        new_player = input("Enter new player")
        player_B = new_player
        player_B_runs = 0
        batsman = player_B