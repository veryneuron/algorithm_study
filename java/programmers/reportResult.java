package programmers;
import java.util.*;

// 92334

class reportResult {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        Arrays.fill(answer, 0);
        Map<String, Set<String>> dict = new HashMap<>();

        for (var r : report) {
            var rArr = r.split(" ");
            if (dict.containsKey(rArr[1])) {
                dict.get(rArr[1]).add(rArr[0]);
            } else {
                dict.put(rArr[1], new HashSet<String>(Arrays.asList(rArr[0])));
            }
        }

        for (var id : id_list) {
            if (dict.containsKey(id) && dict.get(id).size() >= k){
                for (var i : dict.get(id)) {
                    answer[Arrays.asList(id_list).indexOf(i)]++;
                }
            }
        }
        return answer;
    }
}