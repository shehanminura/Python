def start_game():
    global total_runs,wickets,ball,over,batsmen,player_a,player_b
    total_runs=0
    wickets=0
    ball=0
    over=0
    batsman=player_a

def overs_in_match():
    global over ,ball
    while over<2 and wickets < 4 :
        ball_in_over() #passing argument
        over += 1
    
    game_over()
       

def ball_in_over():
    global ball
    ball=0
    while ball<6 and wickets < 4 :
        print_score()
        ball+=1
        score_off_balls()

def score_off_balls():
    global total_runs
    global wickets
    score =input(' Score :')        
    if score.isdigit(): #validation1     
        score=int(score)
        #if 0<=score<5 or score == 6 :
        if score in (0,1,2,3,4,6):
            runs=score 
            total_runs+=runs

    elif score.lower()=="w":
        wickets+=1


def print_score():
        print(f'Total {total_runs}/{wickets} over : {over}.{ball}')


def game_over():
    global over,ball
    if wickets == 4 :
        if ball ==6:
            ball=0
        else:
            over -=1
    elif over == 2:
        ball = 0
    print_score()
    print("Game Over")

def player_change():
    global batsmen,player_a,player_b,score 
    if score == 1 or score == 3:
        if batsmen == player_a:
            batsmen == player_b
        


start_game()
overs_in_match ()
