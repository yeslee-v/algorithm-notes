import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = {};
        ArrayList<double []> list = new ArrayList<>();

        int i, j, cnt = 0, len = stages.length;
        for (i = 1; i <= N; i++) {
            for (j = 0; j < stages.length; j++) {
                if (stages[j] == i) {
                    cnt++;
                }
            }

            // 모든 사용자가 특정 스테이지에서 전부 실패해서
            // 다음 스테이지에 도달한 사람이 아무도 없는 경우 
            double failRate = len == 0 ? 0.0 : ((double)cnt / (double)len); 
            list.add(new double[]{i, failRate});

            len -= cnt;
            cnt = 0;
        }

        Collections.sort(list, (a, b) -> {
            if (a[1] == b[1]) {
                return (int)(a[0] - b[0]);
            }

            return Double.compare(b[1], a[1]);
        });

        answer = new int[N];

        for (int k = 0; k < N; k++) {
            answer[k] = (int)list.get(k)[0];
        }

        return answer;
    }
}