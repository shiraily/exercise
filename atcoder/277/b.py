def func():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input())

    if len(list(set(arr))) != len(arr):
        print("No")
        return

    # print(arr)

    has_err = False

    char1 = ["H", "D", "C", "S"]
    char2 = ["A", "T", "J", "Q", "K"]
    for a in arr:
        # print(a)
        if a[0] not in char1:
            has_err = True
            break
        if isint(a[1]):
            i = int(a[1])
            # print(i)
            if i == 0 or i == 1:
                has_err = True
                break
        else:
            # print("is char")
            if a[1] not in char2:
                has_err = True
                break

    if has_err:
        print("No")
    else:
        print("Yes")

def isint(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True

func()
