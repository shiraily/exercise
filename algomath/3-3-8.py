"""
カードの数を分類しても、同じ数のカードを使う場合があるから効率化しにくい
"""

from collections import defaultdict


def get_cases(n, cards: list[int]):
    if n == 1:
        return cards
    return map(lambda cs: get_cases(n-1, cs), range(n))


def bk_get_cases(cards: list[int]):
    n = 5
    d = defaultdict(int)
    for card in cards:
        d[card] += 1

    nums = sorted(d.keys())

    for i in range(len(nums)):
        #  used = defaultdict(int)
        cnt = 0
        for j in range(1, n + 1):
            sum = i * j
            for k in range(1, n-j + 1):



