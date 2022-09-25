def b():
    x, y, z = list(map(int, input().split()))

    if x >0:
        if y > x or y < 0:
            return x
        else:
            if z > y:
                return -1
            else:
                if z > 0:
                    return x
                else:
                    return x + (abs(z) * 2)
    else:
        if y < x or y > 0:
            return abs(x)
        else:
            if z < y:
                return -1
            else:
                if z < 0:
                    return abs(x)
                else:
                    return abs(x) + (z * 2)

print(b())