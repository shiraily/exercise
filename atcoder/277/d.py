from collections import defaultdict

def func():
    _, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    sum_all = sum(arr)

    d_small = defaultdict(int)
    # modで分類
    for a in arr:
        d_small[a] += 1

    # d_smallの連続部分を列挙
    small_keys = sorted(list(d_small.keys()))
    if len(small_keys) > 0:
        series = [[small_keys[0]]]
    else:
        series = [[]]
    for s in small_keys[1:]:
        last_series = series[-1]
        # print(last_series)
        if s == last_series[-1] + 1:
            last_series.append(s)
        else:
            series.append([s])
    # 最初と最後を結合
    if len(series) > 1:
        if series[0][0] == 0 and series[-1][-1] == m - 1:
            series[-1].extend(series[0][:])
            series[0] = []

    max_sum_remove = -1
    for s in series:
        if len(s) == 0:
            continue

        sum_small = 0
        for ss in s:
            sum_small += ss * d_small[ss]
        if sum_small > max_sum_remove:
            max_sum_remove = sum_small

    print(sum_all - max_sum_remove)


func()
