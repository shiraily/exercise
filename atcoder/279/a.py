def func():
    s = input()

    counter = 0
    for ss in s:
        if ss == "v":
            counter += 1
        else:
            counter += 2

    print(counter)

func()
