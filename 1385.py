n = int(input())
data = [input() for i in range(n)]
mod = 1000000007


def solve(s: str):
    if not s:
        print(0)
        return
    n = len(s)
    total = sum(map(lambda c: ord(c) - ord("a"), s))
    if not total:
        print(0)
        return
    total = total
    dp = [[0] * (total + 1) for _ in range(n + 1)]
    si = [[0] * (total + 1) for _ in range(n + 1)]
    dp[0][total] = 1
    si[0][total] = 1
    for i in range(1, n + 1):
        for j in range(0, total + 1):
            dp[i][j] = (
                si[i - 1][min(j + 25, total)] - (si[i - 1][j - 1] if j else 0)
            ) % mod
            si[i][j] = ((si[i][j - 1] if j else 0) + dp[i][j]) % mod
    print(((dp[n][0] - 1) % mod + mod) % mod)


[solve(s) for s in data]
