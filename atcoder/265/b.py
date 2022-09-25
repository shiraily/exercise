def b():
    n, m, t = list(map(int, input().split()))
    costs = list(map(int, input().split()))  # n - 1こ
    d = dict()
    for i in range(m):
        x, y = list(map(int, input().split()))
        d[x] = y

    sum_time = t
    i = 0

    while sum_time > 0 and i < n - 1:
        # i -> i + 1, 0 -> 1, n-2 -> n-1
        cost = costs[i]
        sum_time -= cost
        if sum_time <= 0:
            break

        i += 1
        room_idx = i + 1
        sum_time += d.get(room_idx, 0)

    if sum_time > 0 and i == n - 1:
        print("Yes")
    else:
        print("No")


b()