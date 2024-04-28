def start_game():
    pass
def overs_in_match():
    over=0
    while over<5 :
        ball_in_over(over) #passing argument
        over+=1
    print(f'over : {over}.0')

def ball_in_over(over):
    ball=0
    while ball<6:
        print(f'over : {over}.{ball}')
        ball+=1

def print_score():
    pass
overs_in_match ()