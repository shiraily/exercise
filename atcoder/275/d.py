def func():
    s_list = []
    for _ in range(9):
        s_list.append(input())

    counter = 0

    # normal
    for w in range(1, 9):
        for r in range(9):
            for c in range(9):
                if s_list[r][c] != "#":
                    continue
                if r + w > 8 or c + w > 8:
                    continue
                if s_list[r + w][c] == "#" and s_list[r][c + w] == "#" \
                        and s_list[r + w][c + w] == "#":
                    counter += 1

    # irregular
    for r in range(9):
        for c in range(9):
            if s_list[r][c] != "#":
                continue
            for rr in range(1, 9):
                for cc in range(1, 9):
                    if is_ng(r + rr) or is_ng(c + cc) or \
                            is_ng(r - cc) or is_ng(c + rr) or \
                            is_ng(r - cc + rr) or is_ng(c + rr + cc):
                        continue
                    if s_list[r + rr][c + cc] == "#" and \
                        s_list[r - cc][c + rr] == "#" and \
                            s_list[r - cc + rr][c + rr + cc] == "#":
                        counter += 1

    print(counter)


def is_ng(tgt):
    return tgt < 0 or tgt > 8


func()


"""
#...#...#
.........
.........
.........
#.......#
.........
.........
.........
#...#...#
"""