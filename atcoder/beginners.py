import os


def welcome():
    a = int(input())
    b, c = map(int, input().split(" "))
    s = input()
    print(f"{a + b + c} {s}")


def product():
    a, b = map(int, input().split(" "))
    if a % 2 == 1:
        print("Odd")
    else:
        remain = x - (500 * aa)
        print("Even")


def coin(a, b, c, x):
    if x % 50 != 0:
        return 0
    result = 0
    for aa in range(min(a, int(x / 500)) + 1):
        print(remain)
        for bb in range(min(b, int(remain / 100)) + 1):
            remain2 = remain - (100 * bb)
            print(remain2)
            if remain2 % 50 == 0 and remain2 / 50 <= c:
                result += 1
    return result


def some_sums(n, a, b):
    return sum(filter(lambda i: is_some(i, a, b), [i for i in range(n + 1)]))


def is_some(i, a, b):
    ret = sum(map(lambda x: int(x), [c for c in str(i)]))
    return a <= ret <= b


def card_for_two(n, arr):
    cards = sorted(arr, reverse=True)
    alice = sum([cards[i * 2] for i in range(0, (n - 1) // 2 + 1)])
    bob = sum([cards[i * 2 + 1] for i in range(0, n // 2)])
    return alice - bob


def kagami_mochi():
    n = int(input())
    d_arr = sorted([int(input()) for i in range(n)], reverse=True)

    current = d_arr[0]
    dan = 1
    for i in range(1, len(d_arr)):
        if d_arr[i] < current:
            dan += 1
        current = d_arr[i]
    return dan


def otoshidama(n, y):
    if y // 10_000 > n:
        return -1, -1, -1
    for a in range(y // 10_000 + 1):
        remain_money = y - (10_000 * a)
        remain_bill = n - a
        if remain_money // 5000 > remain_bill:
            continue
        for b in range(remain_bill + 1):
            remain_money2 = remain_money - b * 5000
            remain_bill2 = remain_bill - b
            if remain_bill2 * 1000 == remain_money2:
                return [a, b, remain_bill2]
    return [-1, -1, -1]


# n, y = map(int, input().split(" "))
# a, b, c = (otoshidama(n, y))
# print(f"{a} {b} {c}")


def day_dream(s: str):
    while len(s) > 0:
        if s.startswith("erase"):
            if len(s) == 5:
                return True
            if s[5] == "r":
                s = s[6:]
            else:
                s = s[5:]
        elif s.startswith("dreamer"):
            if len(s) == 7:
                return True
            if s[7] in ("d", "e"):
                s = s[7:]
            else:
                s = s[5:]
        elif s.startswith("dream"):
            s = s[5:]
        else:
            break
    return len(s) == 0


def travel():
    n = int(input())
    dest = [(0, 0, 0)]

    for t in range(n):
        t, x, y = map(int, input().split(" "))
        dest.append((t, x, y))

    for i in range(1, len(dest)):
        d = dest[i]
        before = dest[i - 1]
        move_cost = abs((d[1] - before[1])) + abs((d[2] - before[2]))
        time_cost = d[0] - before[0]
        if (move_cost > time_cost) or ((time_cost - move_cost) % 2 != 0):
            print("No")
            return
    print("Yes")


travel()