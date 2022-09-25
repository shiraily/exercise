
def world_cup():
    y = int(input())
    if y % 4 == 2:
        print(y)
    else:
        n = (y + 2) // 4 * 4 + 2
        print(n)

# world_cup()


def triangle():
    n, m = list(map(int, input().split()))
    vs = []
    for i in range(m):
        vs.append(tuple(map(int, input().split())))

    vs = set(vs)
    counter = 0

    for i in range(m - 2):
        for j in range(i + 1, m - 1):
            if (i, j) not in vs:
                continue
            for k in range(j + 1, m):
                if ((j, k) not in vs) or ((i, k) not in vs):
                    continue
                counter += 1
    print(counter)


# triangle()

def pair():
    n = int(input())
    arr = list(map(int, input().split()))

    #desc_counter = 0
    #for i in range(n):
    #    ai = arr[i]
    #    ii = n - i
    #    if ai == ii:
    #        desc_counter += 1

    # print((asc_counter * (asc_counter - 1)) // 2 + (desc_counter * (desc_counter - 1)) // 2)

    asc_counter = 0
    counter = 0
    for i in range(n):
        ai = arr[i]
        ii = i + 1
        if ai == ii:
            asc_counter += 1
    for i in range(n):
        ai = arr[i]
        ii = i + 1
        aj = arr[ai - 1]
        if aj == ii and ai != aj:
            # print(ai, aj)
            counter += 1
    #if arr[n-1] == n:
    #    asc_counter += 1
    # print(asc_counter, counter)
    print((asc_counter * (asc_counter - 1)) // 2 + counter // 2)

pair()


import statistics


def avg():
    n = int(input())
    arr = list(map(int, input().split()))

    s = sum(arr)
    avg_n = s // n
    mod_n = s % n

    counter = 0
    def is_ok(arr, non):
        tgt = n - mod_n
        for i, ar in range(arr):
            if ar == tgt and i not in non:
                counter += 1
                is_ok(arr, set(list(non) + i))




avg()