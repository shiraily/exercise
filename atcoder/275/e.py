def func():
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    calc_dp(n, m, arr)


def calc_dp(n, m, arr):
    dp = [[0] * (m + 1) for _ in range(n)]

    dp[0][0] = 1
    if arr[0] <= m:
        dp[0][arr[0]] = 1

    for i in range(1, n):
        for j in range(m + 1):
            ref = dp[i - 1][j]
            if arr[i] > j:
                dp[i][j] = ref
            else:
                ref_back = dp[i - 1][j - arr[i]]
                dp[i][j] = ref or ref_back
    print("yes" if dp[n - 1][m] else "no")
    print(dp)

func()