from collections import defaultdict
import math

def median():
    arr = list(map(int, input().split(" ")))
    sorted_arr = sorted(arr)
    if arr[1] == sorted_arr[1]:
        print("Yes")
        return
    print("No")

# median()

def dist():
    h, w = list(map(int, input().split(" ")))
    komas = []
    for i in range(h):
        if len(komas) == 2:
            break
        s = input()
        j = s.find("o")
        if j >= 0:
            komas.append((i, j))
        j2 = s.rfind("o")
        if j != j2:
            komas.append((i, j2))
            break
    print(komas)
    dist = abs(komas[0][0] - komas[1][0]) + abs(komas[0][1] - komas[1][1])
    print(dist)

# dist()

def max_min():
    q = int(input())
    s = defaultdict(int)
    min_s = math.inf
    max_s = -1
    for i in range(q):
        st = list(map(int, input().split(" ")))
        if st[0] == 1:
            x = st[1]
            s[x] += 1
            if x < min_s:
                min_s = x
            if x > max_s:
                max_s = x
        elif st[0] == 2:
            x = st[1]
            c = st[2]
            if c < s[x]:
                s[x] -= c
            else:
                del(s[x])
                if x == min_s:
                    keys = s.keys()
                    if len(keys) > 0:
                        min_s = min(s.keys())
                    else:
                        min_s = math.inf
                if x == max_s:
                    keys = s.keys()
                    if len(keys) > 0:
                        max_s = max(s.keys())
                    else:
                        max_s = -1
        else:
            print(max_s - min_s)

# max_min()


def fizz_buzz_hard():
    n, a, b = list(map(int,input().split()))
    sum_n = fb_hard(n)
    sum_a = fb_hard((n // a)) * a
    sum_b = fb_hard((n // b)) * b
    lcm_ab = lcm(a, b)
    sum_ab = fb_hard((n // lcm_ab)) * lcm_ab
    print(sum_n - sum_a - sum_b + sum_ab)
"""
    if a % b == 0:
        print(sum_n - sum_b)
    elif b % a == 0:
        print(sum_n - sum_a)
    else:
"""

def fb_hard(n):
    if n == 0:
        return 0
    return  int((1 + n) / 2 * n)

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return a * b // gcd(a, b)

fizz_buzz_hard()