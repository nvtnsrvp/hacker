# Tourist
import math

def print_attractions(N, K, V, attractions):
    i = K*(V-1) - math.floor(K*(V-1)/N)*N
    rem = K
    while rem:
        print(' ' + attractions[i], end='')
        i = (i+1) % N
        rem -= 1
    print()

t = int(input().strip())
for case in range(1, t+1):
    N, K, V = map(int, input().split())
    attractions = [input().strip() for i in range(N)]
    print('Case #' + str(case)+':', end='')
    print_attractions(N, K, V, attractions)
