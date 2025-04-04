function rob(nums: number[]): number {
        let memoArr = new Array(nums.length).fill(-1);
        function getMax(start: number): number {
            if (nums.length - 1 < start) return 0;
            if (memoArr[start] !== -1) return memoArr[start];

            memoArr[start] = Math.max(nums[start] + getMax(start + 2), getMax(start + 1));

            return memoArr[start];
        }

        return getMax(0)
};