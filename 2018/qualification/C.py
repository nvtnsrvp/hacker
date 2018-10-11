# Ethan Searches for a String

# Case #1: ASUC|AB.A|BACUS.A
# Case #2: Impossible
# Case #3: XZY|XYZ.X|YZXZYX.YZXYZYX
# Case #4: Impossible

def ethan(A, B, i, j):
    if i > len(A):
        return True
    if j > len(B):
        return False
    if A[i] == B[j]:
        return ethan(A, B, i+1, j+1)
    if i == 1:
        return ethan(A, B, i, j+1)
    return ethan(A, B, 1, j)

def ethan_test(s):
    ind = s.find(s[0], 1)
    if ind == -1:
        return 'Impossible'
    test = s[:ind] + s
    if test.startswith(s):
        return 'Impossible'
    return test

t = int(input().strip())
for case in range(1, t+1):
    s = input().strip()
    print('Case #' + str(case)+': '+str(ethan_test(s)))
