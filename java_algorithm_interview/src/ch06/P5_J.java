package ch06;

import java.util.*;

public class P5_J {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> results = new HashMap<>();
        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = String.valueOf(chars);

            if (!results.containsKey(key)) results.put(key, new ArrayList<>());

            results.get(key).add(s);
        }

        return new ArrayList<>(results.values());
    }

    public static void main(String[] args) {
        P5_J p5 = new P5_J();

        String[] arg = {"eat", "tea", "tan", "ate", "nat", "bat"};

        List<List<String>> results = p5.groupAnagrams(arg);

        System.out.println(results);
    }
}
