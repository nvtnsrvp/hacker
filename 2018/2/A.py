# Jack's Candy Shop
# https://www.facebook.com/hackercup/problem/638251746380051/

import heapq

def total_sales(tree, C):
    count = {}
    for i in range(len(C)):
        if C[i] not in count:
            count[C[i]] = 0
        count[C[i]] += 1

    total = 0
    def traverse(n):

        for c in tree[n]:

            if n in count and count[n]:

        tree
        if n in count and count[n]:


        for c in tree[n]:


    traverse(0)
    return count


t = int(input().strip())
for case in range(1, t+1):
    N, M, A, B = list(map(int, input().split()))
    C = [(A*i+B) % N for i in range(M)]
    tree = {}
    for i in range(N-1):
        p = int(input())
        if p not in tree:
            tree[p] = [p]
        heapq.heappush(tree[p], -(i+1))
    print('Case #' + str(case)+': '+str(total_sales(tree, C)))
