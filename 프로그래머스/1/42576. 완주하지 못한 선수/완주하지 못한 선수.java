import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> participantMap = new HashMap<>();

        for (String participated : participant) {
            if (participantMap.containsKey(participated)) {
                participantMap.compute(participated, (k, cnt) -> cnt + 1);
            } else {
                participantMap.put(participated, 1);
            }
        }
        for (String completed : completion) {
            if (participantMap.containsKey(completed)) {
                participantMap.compute(completed, (k, cnt) -> cnt - 1);
            }
        }

        for (String key : participantMap.keySet()) {
            if (participantMap.get(key) == 1) answer = key;
        }

        return answer;
    }
}