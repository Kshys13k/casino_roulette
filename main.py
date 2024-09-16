import random
import os

def game():
    money_gained = 0
    bet = 1
    biggest_bet = bet
    games=0
    while(1==1):
        result = roulette_simulation(bet)
        money_gained += result
        games+=1
        if result < 0:
            bet = 2*bet
            if bet > biggest_bet:
                biggest_bet = bet
        else:
            bet = 1

        if games%1000000==0:
            # os.system("clear")
            print("Games played: " + str(games))
            print("Money gained: " + str(money_gained))
            print("Biggest bet: " + str(biggest_bet))


def roulette_simulation(bet):
    result=random.randint(0,37)
    if(result<=18):
        return bet
    if (result > 18):
        return -bet


game()