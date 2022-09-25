def adj(a, b):
    ax = a[0]
    bx = b[0]
    ay = a[1]
    by = b[1]
    if bx > ax + 1 or bx < ax - 1:
        return False
    if by > ay + 1 or by < ay - 1:
        return False
    if bx == ax + 1 and by == ay - 1:
        return False
    if bx == ax - 1 and by == ay + 1:
        return False
    return True


def d():
    n = int(input())

    points = []
    for _ in range(n):
        x, y = input().split()
        points.append((int(x), int(y)))

    group_list = []
    for p in points:
        indexes = []
        for i, group in enumerate(group_list):
            if len(group) == 0:
                continue
            is_adj = False
            for g in group:
                if adj(p, g):
                    is_adj = True
                    break
            if is_adj:
                indexes.append(i)

        l = len(indexes)
        if l == 0:
            group_list.append([p])
        elif l == 1:
            group_list[indexes[0]].append(p)
        else:
            group_list[indexes[0]].append(p)
            first_group = group_list[indexes[0]]
            for i in indexes[1:]:
                for gg in group_list[i]:
                    first_group.append(gg)
                group_list[i] = []

    #max_len = 0
    #for group in group_list:
    #    l = len(group)
    #    if l > max_len:
    #        max_len = l

    counter = 0
    for group in group_list:
        if len(group) > 0:
            counter += 1
    print(counter)


d()


