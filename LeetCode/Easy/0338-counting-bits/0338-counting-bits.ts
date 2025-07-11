function countBits(n: number): number[] {
    const dp = new Array(n + 1).fill(0);
    for (let i = 0; i <= n; i++) {
        dp[i] = dp[i >> 1] + (i & 1);
    }
    return dp;
};