function rob(nums: number[]): number {
    if (nums.length === 1) return nums[0];

    function dp(start: number, end: number) {
        let prev = 0;
        let cur = 0;

        for (let i = start; i < end; i++) {
            [prev, cur] = [cur, Math.max(prev + nums[i], cur)];
        }

        return cur;
    }

    return Math.max(dp(0, nums.length - 1), dp(1, nums.length));
};