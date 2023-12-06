#%%
import re
import pandas as pd

f = open('data/day03/test.txt','r').readlines()

m = len(f[0])-1
n = len(f)

#%% Create Grid
grid = []
for row in f:
    row = row.replace("\n","")
    grid = grid + [list(row)]

#%% Position of Numbers
df_number = pd.DataFrame(columns=['number' , 'x' , 'y' , ])

numbers = []
for row in f:
    numbers_in_row = re.findall('\d+' , row)
    start =0
    for num in numbers_in_row:
        location = row.find(num , start)
        start = location + 1
        length_num = len(num)

def neighbours(grid, r, c):
    vals = sum((row[c -(c>0): c+2]
                for row in grid[r -(r>0):r+2]), [])
    vals.remove(grid[r][c])     # rm itself.
    return vals


