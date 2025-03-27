
class Solution {
    public int solution(int n, int w, int num) {
        int cnt = 0;
        while (num <= n) {
            int targetIndex = (num - 1) % w;
            int reverseIndex = w - targetIndex - 1;
            int upperLevelNum = reverseIndex * 2 + 1;
            num += upperLevelNum;
            cnt++;
        }

        return cnt;
    }
}