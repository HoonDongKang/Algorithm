function containsDuplicate(nums: number[]): boolean {
    return nums.length !== Array.from(new Set(nums)).length
};