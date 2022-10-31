def func():
    a, b, c, d, e, f = list(map(int, input().split()))
    ret = ((a * b * c) - (d * e * f)) %  998244353
    print(ret)

func()
