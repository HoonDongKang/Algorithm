package ch07;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class P1_J {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }

        return null;
    }

    public int[] twoSum2(int[] nums, int target) {
        Map<Integer, Integer> numsMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (numsMap.containsKey(target - nums[i])) {
                return new int[]{numsMap.get(target - nums[i]), i};
            }

            numsMap.put(nums[i], i);
        }

        return null;
    }

    public static void main(String[] args) {
        P1_J p1 = new P1_J();
        int[] nums = {2, 7, 11, 15};
        int[] result = p1.twoSum2(nums, 9);
        System.out.println(Arrays.toString(result));
    }
}
