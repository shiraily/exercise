import math

def func():
    n, m = list(map(int, input().split()))

    root_m = math.floor(math.sqrt(m))
    core_moves = []

    for i in range(0, root_m + 1):
        # print(i)
        j = m - (i ** 2)
        f_root_j = math.floor(math.sqrt(j))
        if f_root_j ** 2 == j:
            core_moves.append((i, f_root_j))

    moves = core_moves[:]
    for m in core_moves:
        i, j = m
        if i > 0:
            moves.append((i * -1, j))
        if j > 0:
            moves.append((i, j * -1))
        if i > 0 and j > 0:
            moves.append((i * -1, j * -1))
    # print(moves)

    start = [(1, 1)]

    guard_n = n + 1
    matrix = [[0] * guard_n for _ in range(guard_n)]

    while len(start) > 0:
        next_start = []
        for s in start:
            i, j = s
            current = matrix[i][j]
            for m in moves:
                dest_i = m[0] + i
                dest_j = m[1] + j
                if 0 < dest_i < guard_n and 0 < dest_j < guard_n:
                    if matrix[dest_i][dest_j] == 0:
                        matrix[dest_i][dest_j] = current + 1
                        next_start.append((dest_i, dest_j))
        start = next_start

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if matrix[i][j] == 0:
                matrix[i][j] = -1

    # 初期化解除
    matrix[1][1] = 0


    for i in range(1, n + 1):
        print(" ".join(list(map(str, matrix[i][1:]))))

func()
