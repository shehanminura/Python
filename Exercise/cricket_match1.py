
def calculation():
    total = 0
    over = 0
    out=0
    player_A="shehan"
    player_B="hasaranga"
    player_A_runs=0
    player_B_runs=0
    batsman=player_A
    total_run=0
    while(over<7):
        ball = 1
        while(7>ball):
            print(over,".",ball)
            mark=input("ball mark=")
            if mark=="out":
                if batsman == player_A:
                    print(f'{player_A} runs ={player_A_runs}')
                    new_player = input("Enter new player")
                    player_A=new_player
                    player_A_runs=0
                    batsman=player_A
                    print(player_A)

                else:
                    print(f'{player_B} runs={player_B_runs}')
                    new_player = input("Enter new player")
                    player_B=new_player
                    player_B_runs=0
                    batsman=player_B
                out = out + 1
                if out==3:
                    break
            else:
                total_run = total_run + int(mark)
                if batsman == player_A:
                    player_A_runs = player_A_runs + int(mark)

                else:
                    player_B_runs = player_B_runs + int(mark)

                if int(mark) == 1 or int(mark) == 3:
                    if batsman==player_A:
                        batsman=player_B
                    else:
                        batsman= player_A

                print(batsman)
                print(player_A,"-",player_A_runs)
                print(player_B,"-",player_B_runs)
                print("total runs -",total_run)
            ball += 1
        over = over + 1
        if out==3:
            print(out)
            break
calculation()