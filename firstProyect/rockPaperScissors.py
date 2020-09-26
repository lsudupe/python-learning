import random


print('Lets play a game. You have to choise between rock, paper and scissors. The computer will choise ramdonly and we will see who wins')


userChoise = input('Write a choise:   ')
r = 'rock'
p = 'paper'
s = 'scissors'

def correctChoise(userChoise):
    lowUserChoise = lower(userChoise)
    if lowUserChoise != r or lowUserChoise != p or lowUserChoise != s:
        print('Please, choise some of the 3 options')
        # aqui igual se deberia hacer un return al principio, crear una funcion para insertar again la opcion
    else:
        winner(lowUserChoise)


def winner(element):
    gameOptions = ['rock', 'paper', 'scissors']
    computerSelection = random.choise(gameOptions)
    