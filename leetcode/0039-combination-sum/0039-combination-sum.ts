function combinationSum(candidates: number[], target: number): number[][] {
    const dp: number[][][] = Array(target + 1)
        .fill(null)
        .map(() => []);

    dp[0] = [[]];

    for (const num of candidates) {
        for (let t = num; t <= target; t++) {
            for (const comb of dp[t - num]) {
                dp[t].push([...comb, num]);
            }
        }
    }

    return dp[target];
};