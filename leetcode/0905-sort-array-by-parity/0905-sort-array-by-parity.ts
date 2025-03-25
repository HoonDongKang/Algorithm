function sortArrayByParity(nums) {
  let leftPointer = 0;
  let rightPointer = nums.length - 1;

  while (leftPointer < rightPointer) {
    if (nums[leftPointer] % 2 !== 0 && nums[rightPointer] % 2 === 0) {
      [nums[leftPointer], nums[rightPointer]] = [
        nums[rightPointer],
        nums[leftPointer],
      ];
    }

    if (nums[leftPointer] % 2 === 0) leftPointer++;
    if (nums[rightPointer] % 2 === 1) rightPointer--;
  }

  return nums;
}