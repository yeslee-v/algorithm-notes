import java.lang.StringBuilder;

class Solution {
  public String mergeAlternately(String word1, String word2) {
    // String에 매번 직접 더하기 O(n^2)
    // StringBuilder: O(n)
    StringBuilder sb = new StringBuilder();

    int word1Len = word1.length();
    int word2Len = word2.length();
    int maxLen = Math.max(word1Len, word2Len);

    for (int i = 0; i < maxLen; i++) {
      if (i < word1Len) {
        sb.append(word1.charAt(i));
      }

      if (i < word2Len) {
        sb.append(word2.charAt(i));
      }
    }

    // StringBuilder -> String
    return sb.toString();
  }
}