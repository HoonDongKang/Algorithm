import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> idxs = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 2) idxs.add(i);
        }

        if (idxs.toArray().length == 0) return new int[]{-1};

        int firstIndex = idxs.get(0);
        int lastIndex = idxs.get(idxs.toArray().length -1 );
        int[] answer = new int[lastIndex - firstIndex + 1];

        for (int i = firstIndex; i <= lastIndex; i++) {
            answer[i - firstIndex] = arr[i];
        }

        return answer;
    }
}