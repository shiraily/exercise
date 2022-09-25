def matrix():
    r, c = list(map(int, input().split()))
    a = []
    a.append(list(map(int, input().split())))
    a.append(list(map(int, input().split())))
    print(a[r - 1][c - 1])

# matrix()

def light():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    person = []
    for i in range(n):
        person.append(tuple(map(int, input().split())))

    lighters = [person[a[i] - 1] for i in range(k)]
    print(lighters)

    r = 0
    for i in range(n):
        tgt = person[i]
        neighbor_r = nn_r(tgt, lighters)
        if neighbor_r > r:
            r = neighbor_r
    print(r)

import math

max_xy = math.inf

def nn_r(tgt, lighters):
    min_dist = max_xy
    min_dist_i = -1
    for i, lighter in enumerate(lighters):
        dist = (abs(tgt[0] - lighter[0]) ** 2) + (abs(tgt[1] - lighter[1]) ** 2)
        if tgt[0] == -41515:
            print(tgt, lighter, math.sqrt(dist), min_dist)
        if dist < min_dist:
            min_dist = dist
            min_dist_i = i
    print(math.sqrt(min_dist), tgt, lighters[min_dist_i], min_dist_i)
    return math.sqrt(min_dist)


light()

def operate():
    x, a, d, n = map(int, input().split())

    last = a + (n - 1) * d
    min_dist = min(a, last)
    max_dist = max(a, last)

    if x <= min_dist:
        return min_dist - x
    if x >= max_dist:
        return x - max_dist
    center = (x - a) // d
    return min(dist(x, a, d, center - 1), dist(x, a, d, center), dist(x, a, d, center + 1))

def dist(x, a, d, center):
    return abs(x - (a + d * center))


print(operate())


def operate2():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_num = len(arr)
    arr_sum = sum(arr)

    for i in range(q):
        x = int(input())
        ret = 0
        for a in range(arr_num):
            # print(a)
            ret += abs(arr[a] - x)
        print(ret)


operate2()