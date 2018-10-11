# Ethan Traverses a Tree
# https://www.facebook.com/hackercup/problem/232395994158286/

import sys

def preorder(tree, current=1):
    if current:
        yield(current)
        yield from preorder(tree, tree[current][0])
        yield from preorder(tree, tree[current][1])

def postorder(tree, current=1):
    if current:
        yield from postorder(tree, tree[current][0])
        yield from postorder(tree, tree[current][1])
        yield(current)

def travesal_order(N, generator):
    order = []
    indices = [0]*N
    i = 0
    for Li in generator:
        order.append(Li)
        indices[Li-1] = i
        i += 1
    return order, indices

def labels(N, K, tree):
    ind2pre, pre2ind = travesal_order(N, preorder(tree))
    ind2post, post2ind = travesal_order(N, postorder(tree))
    # print(ind2pre)
    # print(ind2post)
    label = 1
    labelled = [0]*(N+1)
    for pre in range(1, N+1):
        # print('considering '+str(pre)+' labelled='+str(labelled[pre])+' label='+str(label), end=': ')
        if labelled[pre]:
            # print('skipped')
            continue
        if label > K:
            # print('label > K('+str(K)+')')
            labelled[pre] = K
            continue
        tmp = pre
        while not(labelled[tmp]):
            # print(str(tmp)+' ', end='')
            labelled[tmp] = label
            preind = pre2ind[tmp-1]
            post = ind2post[preind]
            # print('preind='+str(preind)+'post='+str(post))
            if pre == post:
                break
            else:
                tmp = post
        label += 1
        # print('\n')
    if K > label-1:
        return ['Impossible']
    return labelled[1:]


sys.setrecursionlimit(3000)

t = int(input().strip())
for case in range(1, t+1):
    N, K = list(map(int, input().split()))
    tree = dict((i+1, list(map(int, input().split()))) for i in range(N))
    print('Case #' + str(case)+': ', end='')
    print(*labels(N, K, tree))
