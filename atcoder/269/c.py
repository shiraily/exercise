def c():
    n = int(input())
    #  [1, 0, 0, 1]
    bins = bin(n)[2:]

    n_list = list(map(int, [b for b in bins]))
    n_list.reverse()

    keta_arr = list(filter(lambda x: x[1] == 1, [(i, val) for i, val in enumerate(n_list)]))
    keta_arr = list(map(lambda x: x[0], keta_arr))
    #  print(keta_arr)

    for i in range(2 ** len(keta_arr)):
        #  print(i, bin(i))
        bins = bin(i)[2:]
        n_list = [b for b in bins]
        n_list.reverse()

        ans = 0
        for i, n in enumerate(n_list):
            if n == "1":
                ans += 2 ** keta_arr[i]
        print(ans)

c()

"""
print(adjacent((0, 0), (1, 0)))
print(adjacent((0, 0), (1, 1)))
print(adjacent((0, 0), (0, 1)))
print(adjacent((0, 0), (-1, 1)))
print(adjacent((0, 0), (-1, 0)))
print(adjacent((0, 0), (-1, -1)))
print(adjacent((0, 0), (0, -1)))
print(adjacent((0, 0), (1, -1)))
"""