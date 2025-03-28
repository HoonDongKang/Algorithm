import java.util.HashSet;
import java.util.Set;
class Solution {
    public String solution(String my_string, int[] indices) {
        Set<Integer> deleteIndice = new HashSet<>();
        StringBuilder answer = new StringBuilder();

        for (int indice : indices) {
            deleteIndice.add(indice);
        }

        for (int i = 0; i < my_string.length(); i++) {
            if (!deleteIndice.contains(i)) {
                answer.append(my_string.charAt(i));
            }
        }

        return answer.toString();
    }
}