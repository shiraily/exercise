def get_cases(arr):
    num = len(arr)
    if num <= 1:
        return 0
    cnt = 0
    for i in range(num-1):
        for j in range(1, num):
            if arr[i] + arr[j] == 100_000:
                cnt += 1
    return cnt

#print(get_cases([99999, 1, 2]))
#print(get_cases([99999, 1, 1, 99999]))
#print(get_cases([1111, 1, 2]))


import math


#3-3-7
def kazoeage(a, b):
    return math.comb(a + b, a)


#print(kazoeage(3, 2))

