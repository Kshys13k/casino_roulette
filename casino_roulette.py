import random
import argparse
import os

def game(g,v,l):
    money_gained = 0
    bet = 1
    biggest_bet = bet
    games=0
    max_loss = 0
    time_on_minus = 0

    for i in range(g*1000):
        result = roulette_simulation(bet)
        money_gained += result
        games+=1
        if result < 0:
            bet = 2*bet
            if bet > biggest_bet:
                biggest_bet = bet
        else:
            bet = 1

        if l:
            if money_gained < 0:
                time_on_minus += 1
                if money_gained < max_loss:
                    max_loss = money_gained

        if games%(v*1000)==0:
            # os.system("clear")
            print("#####################")
            print("Games played: " + str(games))
            print("Money gained: " + str(money_gained))
            print("Biggest bet: " + str(biggest_bet))
            if l:
                print("Max loss: " + str(max_loss) + ", number of games on minus: " + str(time_on_minus))


def roulette_simulation(bet):
    result=random.randint(0,37)
    if result < 18:
        return bet
    if result >= 18:
        return -bet

def main():
    parser=argparse.ArgumentParser(description="Script simulates martingale betting strategy in european roulette.", epilog="Example: python casino_roulette.py -g 1000 -v 100 -l")
    parser.add_argument('-g', metavar='games', type=int, default=100, help='Games, number of games to play (in thousands); default = 100')
    parser.add_argument('-v', metavar='verbose', type=int, default=100, help='Verbose, how often print an update about gained money (in thousands); default = 100')
    parser.add_argument('-l', action="store_true", help='Loses flag; if active script shows loses statistics')

    args = parser.parse_args()

    game(g=args.g, v=args.v, l=args.l)

if __name__ == "__main__":
    main()

