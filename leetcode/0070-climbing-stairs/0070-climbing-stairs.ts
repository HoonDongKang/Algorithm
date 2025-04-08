function climbStairs(n: number): number {
    if (n <= 0) return 0;

    let dpArr: number[] = new Array(n);
    dpArr[0] = 1;
    dpArr[1] = 2;

    for (let i = 2; i < n; i++) {
        dpArr[i] = dpArr[i - 1] + dpArr[i - 2];
    }

    return dpArr[n - 1];
};