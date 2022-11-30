import math

a = 0
b = 0

def func():
    global a
    global b
    a, b = list(map(int, input().split()))

    left = 0
    right = 10 ** 19
    center = (left + right) // 2
    g_min = math.inf

    while True:
        f_l = f(left)
        f_c = f(center)
        f_r = f(right)
        if left == right:
            break
        if f_l < f_c:
            right = center
            center = (left + right) // 2
            g_min = f_l
        elif f_r < f_c:
            left = center
            center = (left + right) // 2
            g_min = f_r
        else:
            # 収束
            break

    print('{:.10f}'.format(g_min))


def f(x):
    return b * x + a / math.sqrt(1 + x)

func()
