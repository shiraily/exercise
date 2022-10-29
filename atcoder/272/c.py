def func():
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    odds = []
    evens = []

    for a in arr:
        if len(odds) == 2 and len(evens) == 2:
            break
        if a % 2 == 0:
            if (len(evens)) < 2:
                evens.append(a)
        else:
            if (len(odds)) < 2:
                odds.append(a)

    if len(odds) < 2 and len(evens) < 2:
        print(-1)
    else:
        print(max(sum(odds), sum(evens)))

func()
