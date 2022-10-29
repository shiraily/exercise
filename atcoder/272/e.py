import math

def func():
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    # naturals = [i for i in range(n + 1)]

    for i in range(1, m + 1):
        nats = [False for i in range(n + 1)]
        for j in range(n):
            ret = j + 1
            arr[j] += ret
            nats[ret] = True

        for i in range(n + 1):
            if not nats[i]:
                print(i)
                break


        # sets = set(arr)
        # print(arr, naturals)
        #for nat in naturals:
        #    if nat not in sets:
        #        print(nat)
        #        break

func()