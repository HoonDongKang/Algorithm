package ch06;

public class P2_J {
    public void reverseString(char[] s) {
        int start = 0;
        int end = s.length - 1;
        while (start < end) {
            char temp = s[start];
            s[start] = s[end];
            s[end] = temp;

            start++;
            end--;
        }
    }

    public static void main(String[] args) {
        P2_J p1 = new P2_J();
        char[] str = {'h', 'e', 'l', 'l', 'o'};
        p1.reverseString(str);
        System.out.println(str);
    }
}