from collections import defaultdict

def func():
    h, w = list(map(int, input().split()))

    s = []
    t = []
    for i in range(h):
        s.append(input())
    for i in range(h):
        t.append(input())

    ss = [] # 列ごと
    d = defaultdict(int)
    for j in range(w):
        ss_j = []
        tt_j = []
        for i in range(h):
            ss_j.append(s[i][j])
            tt_j.append(t[i][j])
        ss.append("".join(ss_j))
        d["".join(tt_j)] += 1

    # jj_rows = [i for i in range(w)]

    #print(d)
    #print(ss)

    has_diff = False
    for j in range(w):
        tgt = ss[j]
        d[tgt] -= 1
        if d[tgt] < 0:
            has_diff = True
            break

    if has_diff:
        print("No")
    else:
        print("Yes")

func()
