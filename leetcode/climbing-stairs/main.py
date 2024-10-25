def climbStairs(n: int) -> int:
    memo = {}

    def dfs(i):
        if i == n:
            return 1
        if i > n:
            return 0
        if i in memo:
            return memo[i]

        memo[i] = dfs(i + 1) + dfs(i + 2)
        return memo[i]

    return dfs(0)


if __name__ == "__main__":
    assert climbStairs(2) == 2
    # 1. 1 step + 1 step
    # 2. 2 steps

    assert climbStairs(3) == 3
    # 1. 1 step + 1 step + 1 step
    # 2. 1 step + 2 steps
    # 3. 2 steps + 1 step
