import math

def b(r, c):
    if r % 2 == 1:
        if r <= 7:
            c_start = r
            c_end = 16 - r
        else:
            c_end = r
            c_start = 16 - c_end
        if c_start <= c <= c_end:
            return True
        return c % 2 == 1
    else:
        if r <= 8:
            rr = r
            if c < rr or c > 16 - rr:
                if c % 2 == 1:
                    return True
                return False
            return False
        else:
            rr = 16 - r
            if c < rr or c > 16 - rr:
                if c % 2 == 1:
                    return True
                return False
            return False


r, c = list(map(int, input().split()))
ret = b(r, c)
if ret:
    print("black")
else:
    print("white")

