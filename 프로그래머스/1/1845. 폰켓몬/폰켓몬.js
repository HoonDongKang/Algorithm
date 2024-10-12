function solution(nums) {
    let count = nums.length / 2;
    let arr = Array.from(new Set(nums));
    return arr.length >= count ? count : arr.length;
}
