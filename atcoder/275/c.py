from functools import lru_cache

def func():
    n = int(input())
    print(rec(n))


d = dict()
d[0] = 1
d[1] = 2
d[2] = 3
d[3] = 4
d[4] = 5
d[5] = 5


def rec_naive(k):
    if k == 0:
        return 1
    return rec_naive(k // 2) + rec_naive(k // 3)


@lru_cache(maxsize=1000)
def rec(k):
    if k in d:
        return d[k]
    return rec(k // 4) + rec(k // 2 // 3) * 2 + rec(k // 3 // 3)

func()
