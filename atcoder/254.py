import math


# n = int(input())
# print(str(n - (n // 100) * 100).zfill(2))
"""
def int_arr(arr):
    new_arr = [arr[j] + arr[j + 1] for j in range(0, len(arr) - 1)]
    new_arr.insert(0, 1)
    new_arr.append(1)
    return new_arr


def int_arrs(n):
    i = 1
    arr = [1]
    print_arr(arr)
    while i < n:
        arr = int_arr(arr)
        print_arr(arr)
        i += 1


def print_arr(arr):
    print(" ".join([str(i) for i in arr]))


n = int(input())
int_arrs(n)
"""

def k_swap(arr, k):
    n = len(arr)
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        want = sorted_arr[i]
        if arr[i] == want:
            continue
        can_swap = False
        for j in range(1, ((n - i) // k) + 1):
            tgt = i + j * k
            if arr[tgt] == want:
                swap_to_tgt(arr, i, tgt, k)
                can_swap = True
                break
        if not can_swap:
            return "No"
    return "Yes"


def swap(arr, i, k):
    tmp = arr[i]
    arr[i] = arr[i + k]
    arr[i + k] = tmp


def swap_to_tgt(arr, i, tgt, k):
    n = (tgt - i) // k
    for i in range(n):
        swap(arr, tgt - k * (i + 1), k)


def k_swap2(arr, k):
    arrs = []
    n = len(arr)
    for i in range(k):
        arrs.append([arr[j * k + i] for j in range((n - i - 1) // k + 1)])
        arrs[i].sort()
    sorted_arr = sorted(arr)
    for i in range(n):
        tgt = arrs[i % k][i // k]
        if tgt != sorted_arr[i]:
            return "No"
    return "Yes"

"""
 print(k_swap2([10, 2, 3, 4, 5, 5, 1], 6))
print(k_swap2([5, 2, 1, 4, 3], 2))
k = int(input().split(" ")[1])
arr = list(map(int, input().split(" ")))
print(k_swap2(arr, k))
"""


"""
案①
n * nまでの平方数たちを素因数分解する
(各因数 + 1)をかけあわせる
"""

def together(n):
    sqrts = set([i * i for i in range(1, n + 1)])
    count = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if i * j in sqrts:
                count += 1

    print(count * 2 + len(sqrts))

together(254)
together(2 * 10 ** 3)
together(2 * 10 ** 4)