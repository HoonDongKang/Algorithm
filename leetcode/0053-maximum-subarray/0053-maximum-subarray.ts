function maxSubArray(nums: number[]): number {
    let result = nums[0];
    let sum = 0;

    nums.forEach((num) => {
        sum = Math.max(num, sum + num);
        result = Math.max(sum, result);
    });

    return result;
};