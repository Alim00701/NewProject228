import os
from envparse import env
from casino import root
env.read_envfile('settings.env')
balance = os.getenv('MY_MONEY')
while True:
    command = input('Will you play?')
    if command == 'no':
        print(f'You have left on the balance sheet {balance}')
        break
    rate = int(input('Enter number to bet'))
    amount = int(input('Enter the amount to bet'))
    if rate < 1 or rate > 30:
        print('Wrong number to bet')
        continue
    if amount > balance:
        print('Wrong bet amount')
        continue
    balance = root(rate, amount, balance)
