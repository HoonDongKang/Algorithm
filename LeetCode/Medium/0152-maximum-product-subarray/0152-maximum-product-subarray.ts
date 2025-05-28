function maxProduct(nums: number[]): number {
    let maxResult = nums[0];
    let minResult = nums[0];
    let result = nums[0];

    for (let i = 1; i < nums.length; i++) {
        const num = nums[i];

        if (num < 0) {
            [maxResult, minResult] = [minResult, maxResult];
        }

        maxResult = Math.max(num, num * maxResult);
        minResult = Math.min(num, num * minResult);
        result = Math.max(result, maxResult);
    }

    return result;
};