#%%
import re
import pandas as pd

f = open('data/day03/input.txt','r').readlines()

m = len(f[0])-1
n = len(f)

# Create Grid
grid = []
for line in f:
    line = line.replace("\n", "")
    grid = grid + [list(line)]

# Position of Numbers
df_number = pd.DataFrame(columns=['number' , 'col' , 'row' , 'len','check' ])

numbers = []
row = 0
for line in f:
    numbers_in_row = re.findall('\d+', line)
    start =0
    for num in numbers_in_row:
        location = line.find(num, start)
        start = location + 1
        df_number = df_number._append({'number':num , 'col':location , 'row':row , 'len':len(num),'check':False} , ignore_index=True)
    row = row + 1

def neighbours(grid, r, c):
    vals = sum((row[c -(c>0): c+2]
                for row in grid[r -(r>0):r+2]), [])
    vals.remove(grid[r][c])     # rm itself.
    return vals

valid_char = ['0','1','2','3','4','5','6','7','8','9','.']
for i,number in df_number.iterrows():
    for n in range(0,number['len']):
        for c in neighbours(grid, number['row'], number['col'] + n):
            if c not in valid_char:
                df_number.loc[i,'check'] = True

print(df_number[df_number['check']==True]['number'].apply(pd.to_numeric).sum())