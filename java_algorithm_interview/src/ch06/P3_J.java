package ch06;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class P3_J {
    public String[] reorderLogFiles(String[] logs) {
        List<String> letterList = new ArrayList<>();
        List<String> digitList = new ArrayList<>();

        for (String log : logs) {
            if (Character.isDigit(log.split(" ")[1].charAt(0))) {
                digitList.add(log);
            } else {
                letterList.add(log);
            }
        }

        letterList.sort((s1, s2) -> {
            String[] s1x = s1.split(" ", 2);
            String[] s2x = s2.split(" ", 2);

            // s1x == s2x > 0
            // s1x includes s2x > s1x.length = s2x
            // s1x.charAt(0) - s2x.charAt(0)
            // 앞이 먼저면 음수(아스키 상 먼저인 값이 더 작으니깐), 뒤가 먼저면 양수
            int compared = s1x[1].compareTo(s2x[1]);

            System.out.println("====================");
            System.out.println(Arrays.toString(s1x));
            System.out.println(Arrays.toString(s2x));
            System.out.println(compared);

            if (compared == 0) {
                return s1x[0].compareTo(s2x[0]);
            } else {
                return compared;
            }
        });

        letterList.addAll(digitList);

        return letterList.toArray(new String[0]);
    }

    public static void main(String[] args) {
        P3_J p3 = new P3_J();

        String[] strings = {"dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"};

        String[] result = p3.reorderLogFiles(strings);
        System.out.println(Arrays.toString(result));
    }

}
