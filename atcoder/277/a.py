def func():
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(arr.index(x) + 1)


func()
