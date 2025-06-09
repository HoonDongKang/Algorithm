function missingNumber(nums: number[]): number {
    const n = nums.length;
    const sum = nums.reduce((acc, cur) => (acc += cur), 0);
    const expected = (n * (n + 1)) / 2;

    return expected - sum;
};