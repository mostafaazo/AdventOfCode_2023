#%%
f = open('data/day01/input.txt','r').readlines()
dic = {
    "one":"1","two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'
}



sum = 0
for row in f:
    for key , value in dic.items():
        row = row.replace(key,value)
    number = [s for s in row if s.isdigit()]
    value = int(number[0] + number[-1])
    sum = value + sum

print(sum)