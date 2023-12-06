#%%
import re

f = open('data/day02/input.txt','r').readlines()

sum_game = 0
for event in f:

    game_n = int( event.split(":")[0].split(' ')[1])
    sets = event.split(":")[1].split(';')

    event_possible =True
    for set in sets:
        red = green = blue = True
        for cube in set.split(','):
            if 'red'   in cube: red =   int(re.findall(r'\d+', cube)[0]) <=12
            if 'green' in cube: green = int(re.findall(r'\d+', cube)[0]) <=13
            if 'blue'  in cube: blue =  int(re.findall(r'\d+', cube)[0]) <=14
        set_possibe = red * green * blue
        event_possible = event_possible * set_possibe

    if event_possible:
        sum_game = sum_game + game_n

print(sum_game)

