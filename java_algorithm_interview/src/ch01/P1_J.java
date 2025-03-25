package ch01;

public class P1_J {
    // 문자열의 처음과 끝 포인터를 선언
    // 영숫자가 아닌 경우 포인터 이동
    // 양쪽 포인터가 교차할 때까지 각자의 문자 비교 -> 문자가 다르면 false
    // 원시값으로 비교하여 속도가 빠름
    // 시간 복잡도 O(n)
    public boolean isPalindrome(String s) {
        int start = 0;
        int end = s.length() - 1;

        while (start < end) {
            if (!Character.isLetterOrDigit(s.charAt((start)))) {
                start++;
            } else if (!Character.isLetterOrDigit(s.charAt((end)))) {
                end--;
            } else {
                if (Character.toLowerCase(s.charAt(start)) != Character.toLowerCase(s.charAt(end))) return false;
                start++;
                end--;
            }
        }
        return true;
    }

    // 영숫자만 필터링 후, 소문자로 변경
    // 뒤집은 문자열과 원본 문자열 비교
    // 클래스 + 참조형으로 비교, 정규표현식 -> 속도 저하
    public boolean isPalindrome2(String s) {
        String s_filtered = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
        String s_reversed = new StringBuilder(s_filtered).reverse().toString();

        return s_filtered.equals(s_reversed);
    }

    public static void main(String[] args) {
        P1_J p1 = new P1_J();
        P1_J p2 = new P1_J();
        System.out.println(p1.isPalindrome("A man, a plan, a canal: Panama"));
        System.out.println(p2.isPalindrome("A man, a plan, a canal: Panama"));
    }
}
