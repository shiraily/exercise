def func():
    n, m = list(map(int, input().split()))
    nums = []
    humans = []
    for i in range(m):
        arr = list(map(int, input().split()))
        nums.append(arr[0])
        humans.append(set(arr[1:]))
    #print(humans)

    no_same_party = False
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            same_party = False
            for h in humans:
                # print(h)
                #print(i in h)
                #print(j in h)
                if (i in h) and (j in h):
                    same_party = True
                    #print("is_same!")
                    break
            if not same_party:
                no_same_party = True
                break
    if no_same_party:
        print("No")
    else:
        print("Yes")



func()
