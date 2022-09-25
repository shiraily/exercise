def is_two(n):
    return n == 2 or n == 3 or n == 6 or n == 7

def a():
    a, b = list(map(int, input().split()))

    one = a % 2 == 1 or b % 2 == 1
    four = a >= 4 or b >= 4
    two = is_two(a) or is_two(b)

    score = 0
    if one:
        score += 1
    if four:
        score += 4
    if two:
        score += 2
    print(score)

a()

"""
8 4 6
3 1
2 5
1 7
7 8
1 2
4 1
2 6
"""