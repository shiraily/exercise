def func():
    n = int(input())
    hs = list(map(int, input().split()))
    #print(hs)
    highest = sorted(hs, reverse=True)[0]
    #print(highest)
    print(hs.index(highest) + 1)


func()
