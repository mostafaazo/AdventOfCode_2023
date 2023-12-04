#%%
f = open('data/day01/input.txt','r').readlines()

sum = 0
for row in f:
    number = [s for s in row if s.isdigit()]
    value = int(number[0] + number[-1])
    sum = value + sum

print(sum)