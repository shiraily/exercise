from collections import defaultdict
#  import copy
import sys
sys.setrecursionlimit(10**5 * 2 + 1)

d = defaultdict(list)
fins = []
dest = -1


def path(current, prev):
    #  print(current, dest)
    candidates = d[current]
    if len(candidates) < 2:
        if current == dest:
            return current
        return -1
    if current == dest:
        return current

    #  sometimes be large cost
    candidates.remove(prev)
    for c in candidates:
        ret = path(c, current)
        if ret == -1:
            continue
        fins.append(current)
        return 0
    return -1


def c():
    n, x, y = list(map(int, input().split()))

    for i in range(n - 1):
        u, v = list(map(int, input().split()))
        d[u].append(v)
        d[v].append(u)

    #  sentinel
    d[x].append(-1)

    #  current = x
    global dest
    dest = y

    path(x, -1)
    last = [y]

    last.extend(fins)
    last.reverse()

    print(" ".join(list(map(str, last))))


c()

"""
8 4 6
3 1
2 5
1 7
7 8
1 2
4 1
2 6
"""