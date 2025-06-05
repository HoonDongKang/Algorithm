function canJump(nums: number[]): boolean {
    let reach = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i <= reach) {
            reach = Math.max(reach, i + nums[i]);
        }
    }

    return nums.length - 1 <= reach;
};