from collections import defaultdict


def get_next_indexes(arr, indexes):
    # arrに対するindexesの次の配列を返す
    # print(get_next_indexes([[0, 0, 2], [3], [6, 7, 8]], [2, 0, 2]))
    new_indexes = [i for i in indexes]
    for i in range(len(new_indexes)):
        new_indexes[i] += 1
        if new_indexes[i] < len(arr[i]):
            break
        new_indexes[i] = 0
    if sum(new_indexes) == 0:
        return None
    return new_indexes


def c():
    h1, w1 = list(map(int, input().split()))
    a = []
    for i_idx in range(h1):
        a.append(list(map(int, input().split())))

    h2, w2 = list(map(int, input().split()))
    b = []
    for i_idx in range(h2):
        b.append(list(map(int, input().split())))

    # 起点を決める
    starts = []
    for i_idx in range(0, h1 - h2 + 1):
        for j_idx in range(0, w1 - w2 + 1):
            if a[i_idx][j_idx] == b[0][0]:
                starts.append((i_idx, j_idx))

    for start in starts:
        i_a, j_a = start

        # 行列bの最初の行のうち、各indexの要素がAのどこに存在しうるかを取得
        d_j = defaultdict(list)
        # 行列bの最初の行に関して、各要素が存在する位置を取得して辞書化する
        for j_idx in range(1, w2):
            # jを捨てたい、一部
            tgt_b = b[0][j_idx]
            # 少なくとも j_a + j以降で取得可能
            former = d_j[j_idx - 1]
            if (len(former)) > 0:
                # bの最初の行で直前の要素が最初に出現するところよりは少なくとも後ろ
                first_index = former[0] + 1
            else:
                first_index = j_a + j_idx
            for jj in range(first_index, w1):
                tgt_a = a[i_a][jj]
                #  TODO: 不可能な状態をある程度弾きたい
                if tgt_a == tgt_b:
                    d_j[j_idx].append(jj)

        j_arr = list(filter(lambda x: len(x) > 0, [d_j[i] for i in range(1, w2)]))
        len_j_arr = len(j_arr)
        # どんどん最初の行の候補を生成していく
        if len_j_arr < w2 - 1:
            # bの最初の行の要素のうち、存在しないものがあった
            continue
        current_indexes = [0 for _ in range(1, w2)]  # TODO 効率的にかけそう
        # TODO reducer使いたい
        num_patterns = 1
        for i_idx in range(len_j_arr):
            num_patterns *= (len(j_arr[i_idx]) + 1)
        # TODO generator書きたい
        correct_j_arr = []
        for i_idx in range(num_patterns):
            this_arr = [j_arr[j][current_indexes[j]] for j in range(len_j_arr)]
            # check row
            is_ok = True
            for j_idx in range(len_j_arr -1):
                if this_arr[j_idx + 1] <= this_arr[j_idx]:
                    is_ok = False
                    break
            if is_ok:
                correct_j_arr.append(this_arr)

            current_indexes = get_next_indexes(j_arr, current_indexes)
            if current_indexes is None:  # いらないかも
                break

        # 行列bの最初の列のうち、各indexの要素がAのどこに存在しうるかを取得
        d_i = defaultdict(list)
        for i_idx in range(1, h2):
            tgt_b = b[i_idx][0]
            former = d_i[i_idx - 1]
            if (len(former)) > 0:
                first_index = former[0] + 1
            else:
                first_index = i_a + i_idx
            for ii in range(first_index, h1):
                tgt_a = a[ii][j_a]
                if tgt_a == tgt_b:
                    d_i[i_idx].append(ii)

        i_arr = list(filter(lambda x: len(x) > 0, [d_i[i] for i in range(1, h2)]))
        len_i_arr = len(i_arr)
        if len_i_arr < h2 - 1:
            continue
        current_indexes = [0 for _ in range(1, h2)]  # TODO 効率的にかけそう
        num_patterns = 1
        for i_idx in range(len_i_arr):
            num_patterns *= (len(i_arr[i_idx]) + 1)
        correct_i_arr = []
        for _ in range(num_patterns):
            this_arr = [i_arr[i][current_indexes[i]] for i in range(len_i_arr)]
            is_ok = True
            for j_idx in range(len_i_arr - 1):
                if this_arr[j_idx + 1] <= this_arr[j_idx]:
                    is_ok = False
                    break
            if is_ok:
                correct_i_arr.append(this_arr)

            current_indexes = get_next_indexes(i_arr, current_indexes)
            if current_indexes is None:  # いらないかも
                break

        for j_arr in correct_j_arr:
            for i_arr in correct_i_arr:
                has_incorrect = False
                for j_idx, j in enumerate(j_arr):
                    for i_idx, r in enumerate(i_arr):
                        if a[r][j] != b[i_idx + 1][j_idx + 1]:
                            has_incorrect = True
                            break
                if not has_incorrect:
                    return True
    return False


# print(c())

import math


def get_next_bins(indexes):
    # 次の2進数を得る
    new_indexes = [i for i in indexes]
    for i in range(len(new_indexes)):
        new_indexes[i] = (new_indexes[i] + 1) % 2
        if new_indexes[i] == 1:
            break
    return new_indexes


def cc():
    h1, w1 = list(map(int, input().split()))
    a = []
    for i_idx in range(h1):
        a.append(list(map(int, input().split())))

    h2, w2 = list(map(int, input().split()))
    b = []
    for i_idx in range(h2):
        b.append(list(map(int, input().split())))

    # todo use bit
    use_row_flags = [0 for _ in range(h1)]

    for i in range(2 ** h1):
        # 最初の行は一番最後にチェックされる
        use_row_flags = get_next_bins(use_row_flags)
        if sum(use_row_flags) != h2:
            continue
        use_row_indexes = []
        for flag_idx, flag in enumerate(use_row_flags):
            if flag == 1:
                use_row_indexes.append(flag_idx)

        use_col_flags = [0 for _ in range(w1)]  # reset
        for j in range(2 ** w1):
            use_col_flags = get_next_bins(use_col_flags)
            if sum(use_col_flags) != w2:
                continue
            use_col_indexes = []
            for flag_idx, flag in enumerate(use_col_flags):
                if flag == 1:
                    use_col_indexes.append(flag_idx)
            has_invalid = False
            for r_idx, r in enumerate(use_row_indexes):
                for c_idx, c in enumerate(use_col_indexes):
                    if a[r][c] != b[r_idx][c_idx]:
                        has_invalid = True
                        break
            if not has_invalid:
                return True

    return False


print(cc())


"""
4 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
2 3
6 8 9
16 18 19

Yes

3 3
1 1 1
1 1 1
1 1 1
1 1
2

No

test

3 9
1 1 1 2 2 2 3 3 3
1 1 1 2 2 2 3 3 3
1 1 1 2 2 2 3 3 3
2 3
1 2 3
1 2 3

3 9
1 2 3 1 2 3 1 2 3
1 2 3 1 2 3 1 2 3
1 2 3 1 2 3 1 2 3
2 3
1 2 3
1 2 3

3 9
1 2 3 1 2 3 1 2 3
7 7 7 7 7 7 7 7 7
1 2 3 1 2 3 4 5 6
2 3
1 2 3
4 5 6


3 9
1 2 3 1 2 3 -1 -1 -1
7 7 7 7 7 7 1 2 3
4 5 3 1 2 3 4 5 6
2 3
1 2 3
4 5 6
"""