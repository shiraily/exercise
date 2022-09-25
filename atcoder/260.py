from collections import defaultdict

def st():
    s = input()

    d = defaultdict(int)

    d[s[0]] += 1
    d[s[1]] += 1
    d[s[2]] += 1

    for k, v in d.items():
        if v == 1:
            return k
    return -1

print(st())


def students():
    n, x, y, z = list(map(int, input().split()))

    maths = [(idx + 1, score) for idx, score in enumerate(list(map(int, input().split())))]
    engs = [(idx + 1, score) for idx, score in enumerate(list(map(int, input().split())))]
    sums = [(idx + 1, maths[idx][1] + engs[idx][1]) for idx in range(n)]

    maths.sort(key=lambda t: t[1] * (n + 1) + (n - t[0]), reverse=True)
    engs.sort(key=lambda t: t[1] * (n + 1) + (n - t[0]), reverse=True)
    sums.sort(key=lambda t: t[1] * (n + 1) + (n - t[0]), reverse=True)

    # print(maths)
    # print(engs)
    # print(sums)

    winners = list(map(lambda t: t[0], maths[:x]))
    winners_set = set(winners)

    # print(winners)

    num_eng = 0
    i = 0
    while num_eng < y:
        tgt = engs[i][0]
        if tgt not in winners_set:
            winners.append(tgt)
            winners_set.add(tgt)
            num_eng += 1
        i += 1

    num_sum = 0
    i = 0
    while num_sum < z:
        # print(i)
        tgt = sums[i][0]
        if tgt not in winners_set:
            winners.append(tgt)
            num_sum += 1
        i += 1

    for w in sorted(winners):
        print(w)


students()


###


from collections import defaultdict


def jewels():
    n, x, y = list(map(int, input().split()))
    if n == 1:
        print(0)
        return
    reds = defaultdict(int)
    reds[n] = 1
    blues = defaultdict(int)

    while avail_jewels(reds) or avail_jewels(blues):
        # print(reds.items(), blues.items())
        for k, v in sorted(list(reds.items()), reverse=True):
            if k > 1:
                # print("hakka1")
                blues[k] += x * v
                reds[k] = 0
                reds[k - 1] += v
        # print(reds, blues)
        for k, v in sorted(list(blues.items()), reverse=True):
            if k > 1:
                # print("hakka2")
                reds[k - 1] += v
                blues[k] = 0
                blues[k - 1] += y * v
        # print(reds, blues)
    print(blues[1])


def avail_jewels(jewels):
    num = 0
    for k, v in jewels.items():
        if k > 1 and v > 0:
            num += 1
    return num > 0


# jewels()


def cards():
    n, k = list(map(int, input().split()))
    ps = list(map(int, input().split()))

    yamas = []
    ans = [-1] * n
    for i, p in enumerate(ps):
        min_k = 10 ** 5 + 1
        min_k_idx = -1
        for idx, yama in enumerate(yamas):
            if len(yama) < 1:
                continue
            key = yama[-1]
            if p <= key < min_k:
                min_k = key
                min_k_idx = idx
        if min_k_idx == -1:
            yamas.append([p])

        tgt = yamas[min_k_idx]
        tgt.append(p)
        if len(tgt) < k:
            continue
        turn = i + 1
        for card in tgt:
            ans[card-1] = turn
        yamas.pop(min_k_idx)

    print(*ans)


cards()