# Evening of the Living Dead
# https://www.facebook.com/hackercup/problem/359971574540051/

import numpy as np

def calculate_p_at_least_one_yard_is_safe(p_no_yard_is_safe):
    return 1 - p_no_yard_is_safe

def calculate_p_no_yard_is_safe(p_no_zombie_can_reach_yard_i):
    return np.prod(1-p_no_zombie_can_reach_yard_i)

def calculate_p_no_zombie_can_reach_yard_i(p_zombie_j_cannot_reach_yard_i):
    p_no_zombie_can_reach_yard_i = np.sum(np.log(p_zombie_j_cannot_reach_yard_i), axis=0)
    return np.exp(p_no_zombie_can_reach_yard_i)

def calculate_p_zombie_j_cannot_reach_yard_i(N, fences, zombies):
    p_zombie_j_cannot_reach_yard_i = np.zeros([len(zombies), N])
    count = 0
    for j, Hj in zombies:
        j -= 1
        plog = 0
        for i in range(j, 0, -1):
            Ai, Bi = fences[i-1]
            if plog == None or Hj < Ai:
                plog = None
            elif Hj > Bi:
                plog = plog
            else:
                plog += np.log(Hj-Ai+1) - np.log(Bi-Ai+1)
            # print("left j-1", j, "i-1", i-1, "Ai", Ai, "Bi", Bi, "Hj", Hj, "Hj-Ai+1/Bi-Ai+1", str(Hj-Ai+1)+"/"+str(Bi-Ai+1), "plog", plog)
            if plog == None:
                p_zombie_j_cannot_reach_yard_i[count, i-1] = 1
            else:
                p_zombie_j_cannot_reach_yard_i[count, i-1] = 1 - np.exp(plog)
        plog = 0
        for i in range(j+1, N):
            Ai, Bi = fences[i-1]
            if plog == None or Hj < Ai:
                plog = None
            elif Hj > Bi:
                plog = plog
            else:
                plog += np.log(Hj-Ai+1) - np.log(Bi-Ai+1)
            # print("right j-1", j, "i-1", i-1, "Ai", Ai, "Bi", Bi, "Hj", Hj, "Hj-Ai+1/Bi-Ai+1", str(Hj-Ai+1)+"/"+str(Bi-Ai+1), "plog", plog)
            if plog == None:
                p_zombie_j_cannot_reach_yard_i[count, i] = 1
            else:
                p_zombie_j_cannot_reach_yard_i[count, i] = 1 - np.exp(plog)
        count += 1
    return p_zombie_j_cannot_reach_yard_i

def at_least_one_yard_is_safe(fences, zombies):
    zombies.sort()
    # print(fences, zombies)
    p_zombie_j_cannot_reach_yard_i = calculate_p_zombie_j_cannot_reach_yard_i(N, fences, zombies)
    # print(p_zombie_j_cannot_reach_yard_i)
    p_no_zombie_can_reach_yard_i = calculate_p_no_zombie_can_reach_yard_i(p_zombie_j_cannot_reach_yard_i)
    # print(np.exp(p_no_zombie_can_reach_yard_i))
    p_no_yard_is_safe = calculate_p_no_yard_is_safe(p_no_zombie_can_reach_yard_i)
    p_at_least_one_yard_is_safe = calculate_p_at_least_one_yard_is_safe(p_no_yard_is_safe)
    return p_at_least_one_yard_is_safe * 1000000007

t = int(input().strip())
for case in range(1, t+1):
    N, M = list(map(int, input().split()))
    fences = [list(map(int, input().split())) for i in range(N-1)]
    zombies = [list(map(int, input().split())) for i in range(M)]
    print('Case #' + str(case)+': '+str(at_least_one_yard_is_safe(fences, zombies)))

Case #1: 500000003.5
Case #2: 125000000.875
Case #3: 770833338.7291667
Case #4: 900972637.1357718
Case #5: 843558521.3966658
Case #6: 791797492.4825579

# Case #1: 500000004
# Case #2: 125000001
# Case #3: 666666672
# Case #4: 417224706
# Case #5: 441220242
# Case #6: 292643605

