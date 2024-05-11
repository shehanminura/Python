
class CricketMatch():
    def start_game():
        global total_runs,wickets,ball,over,batsman,player_a,player_b,player_a_runs,player_b_runs,player_a_ball,player_b_ball,star_a,star_b
        total_runs=0
        wickets=0
        ball=0
        over=0
        player_a="shehan"
        player_b="hasaranga"
        player_a_runs=0
        player_b_runs=0
        batsman=player_a
        player_a_ball=0
        player_b_ball=0
        star_a=""
        star_b=""

    def overs_in_match():
        global over ,ball
        while over<2 and wickets < 4 :
            ball_in_over() #passing argument
            over += 1
            over_change_player()
        
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
                player_runs(score)
                player_change(score)

        elif score.lower()=="w":
            wickets+=1
            player_change_wickets()


    def print_score():
            star_mark()
            print(f'Total {total_runs}/{wickets} over : {over}.{ball}  {player_a} - {player_a_runs} ({player_a_ball}) {star_a} / {player_b} - {player_b_runs} ({player_b_ball}) {star_b}')


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

    def player_change(score):
        global batsman,player_a,player_b
        if score == 1 or score == 3:
            if batsman == player_a:
                batsman = player_b

            else:
                batsman=player_a
            



    def player_runs(score):
        global batsman,player_a,player_b,player_a_runs,player_b_runs,player_a_ball,player_b_ball
        
        if batsman==player_a:
            player_a_runs=player_a_runs+score
            player_a_ball=player_a_ball+1

        else:
            player_b_runs=player_b_runs+score
            player_b_ball=player_b_ball+1

        star_mark()


    def player_change_wickets():
        global batsman, player_a, player_b, player_a_runs, player_b_runs,player_a_ball,player_b_ball
        if batsman==player_a:
            print(f'{player_a} Runs={player_a_runs}')
            new_player=input("Enter new player :")
            player_a_runs=0
            player_a_ball=0
            player_a=new_player
            batsman=player_a
            print(player_a)
        else:
            print(f'{player_b} Runs={player_b_runs}')
            new_player=input("Enter new player :")
            player_b_runs=0
            player_b_ball=0
            player_b = new_player
            batsman=player_b
            print(player_b)

    def over_change_player():
        global batsman,player_a,player_b
        if batsman==player_a:
            batsman=player_b
        else:
            batsman=player_a

    def star_mark():
        global star_a,star_b,player_a,batsman
        if batsman ==  player_a:
            star_a="*"
            star_b=""
        else:
            star_b="*"
            star_a=""

class T20 :
    pass

def main():
    firstBat =CricketMatch() #instance (object)
    print(total_runs)

start_game()
overs_in_match ()
