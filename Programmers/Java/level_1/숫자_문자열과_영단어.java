import java.util.HashMap;

/*
 * HashMap 사용하지 않고 처음 선언할 때부터 값 넣기
 * replaceAll 메서드 활용 가능
 */
class Solution {
    public int solution(String s) {
        int answer = 0;

        HashMap<String, Integer> numbers = new HashMap<String, Integer>();

        numbers.put("zero", 0);
        numbers.put("one", 1);
        numbers.put("two", 2);
        numbers.put("three", 3);
        numbers.put("four", 4);
        numbers.put("five", 5);
        numbers.put("six", 6);
        numbers.put("seven", 7);
        numbers.put("eight", 8);
        numbers.put("nine", 9);

        String tmp = "";
        for (String key: numbers.keySet()) {
            if (-1 < s.indexOf(key)) {
                Integer value = numbers.get(key);

                tmp = tmp.length() != 0 ? tmp.replace(key, Integer.toString(value)) : s.replace(key, Integer.toString(value));
            }
        }

        answer = tmp.length() != 0 ? Integer.parseInt(tmp) : Integer.parseInt(s);

        return answer;
    }
}