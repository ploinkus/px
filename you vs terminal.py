#game you play with the terminal
import random

def roll():
    min_roll = 1
    max_roll = 6
    amount = random.randint(min_roll, max_roll)
    return amount


def player_score():
    playerscore = 0
    rollvalue = roll()
    if rollvalue == 1:
        playerscore = 0
        print('You lost.')
        print('I win!!!!')
    else:
        playerscore += rollvalue
        print('your score is now ' + str(playerscore))
    return playerscore

def terminal_score():
    terminalscore = 0
    rollvalue = roll()
    if rollvalue == 1:
        print('Aw man, I lost!')
        print('You win.')
    else:
        terminalscore += rollvalue
        print('My score is now ' + str(terminalscore))
        return terminalscore

p1 = 0
terminal_ = 0

while p1 or terminal_ < 50:
    def gamecontinue():
        roller_continue = input('Do you want to roll? ')
        if roller_continue == 'yes':
            p1 = player_score()
            terminal_ = terminal_score()
            print(str(p1))
            print(str(terminal_))

    gamecontinue()

