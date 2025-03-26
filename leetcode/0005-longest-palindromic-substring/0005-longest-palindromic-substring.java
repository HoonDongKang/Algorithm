class Solution {
    int maxLen, left;

    public String longestPalindrome(String s) {
        int length = s.length();
        if (length < 2) return s;

        for (int i = 0; i < length - 1; i++) {
            expandPalindrome(s, i, i + 1);
            expandPalindrome(s, i, i + 2);
        }

        return s.substring(left, left + maxLen);
    }

    public void expandPalindrome(String s, int j, int k) {
        while (0 <= j && k < s.length() && s.charAt(j) == s.charAt(k)) {
            j--;
            k++;
        }
        if (maxLen < k - j - 1) {
            left = j + 1;
            maxLen = k - j - 1;
        }
    }
}