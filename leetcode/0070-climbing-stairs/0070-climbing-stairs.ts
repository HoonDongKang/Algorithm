function climbStairs(n: number): number {
    if (n <= 0) return 0;
    if (n === 1) return 1;
    if (n === 2) return 2;

    let prev1 = 1;
    let prev2 = 2;

    for (let i = 3; i < n + 1; i++) {
        let currentValue = prev1 + prev2;

        prev1 = prev2;
        prev2 = currentValue;
    }

    return prev2;
};