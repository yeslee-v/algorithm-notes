/*
 * 배열의 길이가 2로 고정 + 값 크기 단순 비교 >> Math 함수 쓰면 간단하게 작성 가능할 듯
 */
class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;

        int maxWallet, minWallet, maxBill, minBill;
        if (wallet[0] < wallet[1]) {
            maxWallet = wallet[1];
            minWallet = wallet[0];
        } else {
            maxWallet = wallet[0];
            minWallet = wallet[1];
        }

        if (bill[0] < bill[1]) {
            maxBill = bill[1];
            minBill = bill[0];
        } else {
            maxBill = bill[0];
            minBill = bill[1];
        }

        while ((minWallet < minBill) || (maxWallet < maxBill)) {
            if (bill[1] < bill[0]) {
                bill[0] /= 2;

                if (bill[0] < bill[1]) {
                    maxBill = bill[1];
                    minBill = bill[0];
                } else {
                    maxBill = bill[0];
                    minBill = bill[1];
                }
            } else {
                bill[1] /= 2;

                if (bill[0] < bill[1]) {
                    maxBill = bill[1];
                    minBill = bill[0];
                } else {
                    maxBill = bill[0];
                    minBill = bill[1];
                }
            }

            answer++;
        }

        return answer;
    }
}