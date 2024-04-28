def start_game():
    global total_runs
    total_runs=0
    global wickets
    wickets=0
def overs_in_match():
    over=0
    while over<5 :
        ball_in_over(over) #passing argument
        over+=1
    print(f'over : {over}.0')

def ball_in_over(over):
    ball=0
    while ball<6:
        print(f'Total {total_runs}/{wickets} over : {over}.{ball}')
        score_off_balls()
        
        ball+=1

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

    elif score.lower()=="out":
       wickets+=1
                
    


def print_score():
    pass
start_game()
overs_in_match ()