from collections import defaultdict

def func():
    n = int(input())
    d = defaultdict(list)
    for _ in range(n):
        a, b = list(map(int, input().split()))
        d[a].append(b)
        d[b].append(a)

    paths = set()
    max_f = 1
    start = {1}

    while True:
        if len(start) == 0:
            break
        new_start = set()
        for s in start:
            paths.add(s)
            if s > max_f:
                max_f = s
            for n in d.get(s, []):
                if n not in paths:
                    new_start.add(n)
        start = new_start
    print(max_f)

func()
