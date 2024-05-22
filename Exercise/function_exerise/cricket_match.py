
class CricketMatch():
    def start_game(self):
        #global total_runs,wickets,ball,over,batsman,player_a,player_b,player_a_runs,player_b_runs,player_a_ball,player_b_ball,star_a,star_b
        self.total_runs=0
        self.wickets=0
        self.ball=0
        self.over=0
        self.player_a_runs=0
        self.player_b_runs=0
        self.player_a_ball=0
        self.player_b_ball=0
        self.star_a=""
        self.star_b=""
        self.player_n=""
        self.players_name=[]
        self.add_players_Name()
        self.player_a=self.players_name[0]
        self.player_b=self.players_name[1]
        self.batsman=self.player_a
        
        self.bollers_name=[]
        


    def add_bollers(self):
            baller=input("Enter Boller Name:")
            if  baller not in  self.bollers_name:
                self.bollers_name.append(baller)
            else:
                print("is in")

    def add_players_Name(self):
        for i in range (1,6):
            player=input(f'player{i}:')
            self.players_name.append(player)
 

    def overs_in_match(self):
        #global over ,ball
        while self.over<2 and self.wickets < 4 :
            self.add_bollers()
            self.ball_in_over() #passing argument
            self.over += 1
            self.over_change_player()
        
        self.game_over()
        
    def ball_in_over(self):
        #global ball
        self.ball=0
        while self.ball<6 and self.wickets < 4 :
            self.print_score()
            self.ball+=1
            self.score_off_balls()

    def score_off_balls(self):
        #global total_runs
        #global wickets
        
        score =input(' Score :')        
        if score.isdigit(): #validation1     
            score=int(score)
            #if 0<=score<5 or score == 6 :
            if score in (0,1,2,3,4,6):
                runs=score 
                self.total_runs+=runs
                self.player_runs(score)
                self.player_change(score)

        elif score.lower()=="w":
            self.wickets+=1
            if self.wickets<4:
                self.player_change_wickets()


    def print_score(self):
            
            self.star_mark()
            print(f'Total {self.total_runs}/{self.wickets} over : {self.over}.{self.ball}  {self.player_a} - {self.player_a_runs} ({self.player_a_ball}) {self.star_a} / {self.player_b} - {self.player_b_runs} ({self.player_b_ball}) {self.star_b}')

    def game_over(self):
        #global over,ball
        
        if self.wickets == 4 :
            if self.ball ==6:
                self.ball=0
            else:
                self.over -=1
        elif self.over == 2:
            self.ball = 0
        self.print_score()
        print("Game Over")

    def player_change(self,score):
        #global batsman,player_a,player_b
        if score == 1 or score == 3:
            if self.batsman == self.player_a:
                self.batsman = self.player_b

            else:
                self.batsman=self.player_a            



    def player_runs(self,score):
        #global batsman,player_a,player_b,player_a_runs,player_b_runs,player_a_ball,player_b_ball
        
        if self.batsman==self.player_a:
            self.player_a_runs=self.player_a_runs+score
            self.player_a_ball=self.player_a_ball+1

        else:
            self.player_b_runs=self.player_b_runs+score
            self.player_b_ball=self.player_b_ball+1

        self.star_mark()


    def player_change_wickets(self):
        #global batsman, player_a, player_b, player_a_runs, player_b_runs,player_a_ball,player_b_ball
        if self.batsman==self.player_a:
            print(f'{self.player_a} Runs={self.player_a_runs}')
            self.player_a=self.players_name[self.wickets+1]
            self.player_a_runs=0
            self.player_a_ball=0
            self.batsman=self.player_a
            print(self.player_a)
        else:
            print(f'{self.player_b} Runs={self.player_b_runs}')
            self.player_b=self.players_name[self.wickets+1]
            self.player_b_runs=0
            self.player_b_ball=0
            self.batsman=self.player_b
            print(self.player_b)

    def over_change_player(self):
        #global batsman,player_a,player_b
        if self.batsman==self.player_a:
            self.batsman=self.player_b
        else:
            self.batsman=self.player_a

    def star_mark(self):
        #global star_a,star_b,player_a,batsman
        if self.batsman ==  self.player_a:
            self.star_a="*"
            self.star_b=""
        else:
            self.star_b="*"
            self.star_a=""

class T20 :
    pass

def main():
    firstBat =CricketMatch() #instance (object)
    secondBat =CricketMatch() 
    firstBat.start_game()
    firstBat.overs_in_match ()
    secondBat.start_game()
    secondBat.overs_in_match ()
    print(firstBat)
    print(secondBat)



if __name__ == "__main__":
    main()
    
