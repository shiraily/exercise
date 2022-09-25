from collections import defaultdict


def c():
    n, x, y = list(map(int, input().split()))
    d = defaultdict(list)

    for i in range(n - 1):
        u, v = list(map(int, input().split()))
        d[u].append(v)
        d[v].append(u)

    #  sentinel
    d[x].append(-1)
    queue = [-1]
    dest = y
    current = x

    while True:
        print(current, queue)
        if current == dest:
            queue.append(current)
            break

        candidates = d[current]
        num = len(candidates)

        if num == 0:
            #  invalid middle node. back to prev
            current = queue.pop()
        elif num == 1:
            next_node = candidates.pop()
            if next_node == queue[-1]:
                current = queue.pop()
            else:
                #  only proceed
                queue.append(current)
                current = next_node
        else:
            prev = queue[-1]
            queue.append(current)
            next_node = candidates.pop()
            if next_node == prev:
                next_node = candidates.pop()
            current = next_node

    del queue[0]

    print(" ".join(list(map(str, queue))))


c()
