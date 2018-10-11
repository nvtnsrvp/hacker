# Let It Flow
# https://www.facebook.com/hackercup/problem/180494849326631/

import numpy as np

def num_flows(N, grid):
    mem = [1, 0, 0]
    for j in range(N):
        mem = [
            mem[1]*grid[0,j],
            (mem[0]*grid[0,j] + mem[2]*grid[1,j]) % 1000000007,
            mem[1]*grid[1,j]
        ]
        if sum(mem) == 0:
            return 0
    return mem[-1] % 1000000007

t = int(input().strip())
for case in range(1, t+1):
    N = int(input().strip())
    grid = np.matrix([[int(j == '.') for j in input()] for i in range(3)])
    grid = np.vstack((grid[0,:]&grid[1,:], grid[1,:]&grid[2,:]))
    print('Case #' + str(case)+': '+str(num_flows(N, grid)))

