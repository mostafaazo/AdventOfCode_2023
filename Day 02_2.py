#%%
import re

f = open('data/day02/input.txt','r').readlines()

power = 0
for event in f:
    sets = event.split(":")[1].split(';')
    set_red = set_blue = set_green = []
    for set in sets:
        red = green = blue = []
        for cube in set.split(','):
            if 'red'   in cube: red   =  [int(re.findall(r'\d+', cube)[0])]
            if 'green' in cube: green =  [int(re.findall(r'\d+', cube)[0])]
            if 'blue'  in cube: blue  =  [int(re.findall(r'\d+', cube)[0])]
        set_red = red + set_red
        set_green=green+ set_green
        set_blue = blue + set_blue
    set_power = max(set_red) * max(set_green) * max(set_blue)
    power = power + set_power

print(power)