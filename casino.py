from random import random as r, choice


def root(rate, amount, balance):
    lst = [i for i in range(1, 31)]
    win_rate = r.choice(lst)
    if win_rate == rate:
        print('You win')
        return balance + amount
    else:
        print('you lose')
