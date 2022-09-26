package programmers;
import java.util.*;
import java.util.stream.Collectors;

class biggestNum {
    public static String solution(int[] numbers) {
        List<String> numString = Arrays.stream(numbers).boxed().map(Object::toString).collect(Collectors.toList());
        numString.sort((o1, o2) -> o2.repeat(3).compareTo(o1.repeat(3)));
        String result = String.join("", numString);
        int index = 0;
        for (var ch : result.toCharArray()) {
            if (ch == '0') {
                index++;
            } else {
                break;
            }
        }
        String answer = result.substring(index);
        if (answer.length() == 0) {
            return "0";
        } else {
            return answer;
        }
    }

    public static void main(String[] args) {
        int[] input = {6, 10, 2};
        System.out.println(solution(input));
    }
}