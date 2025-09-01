# 1768 문자열 교대로 합치기

## 🔗 문제 링크
- [LeetCode 1768](https://leetcode.com/problems/merge-strings-alternately/)

## 🎯 문제 분석
- 두 문자열을 교대로 합치기
- word1의 첫 번째 문자, word2의 첫 번째 문자, word1의 두 번째 문자...
- 한 문자열이 더 길면 나머지 문자들을 뒤에 이어붙임

**입출력 예시:**
```
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Input: word1 = "ab", word2 = "pqrs"  
Output: "apbqrs"
```

## �️ Java 구현
📁 **전체 코드**: [1768_merge_strings_alternately.java](../code/1768_merge_strings_alternately.java)

```java
// 핵심 로직: StringBuilder로 문자열 교대 합치기
public String mergeAlternately(String word1, String word2) {
    StringBuilder sb = new StringBuilder();
    int maxLen = Math.max(word1.length(), word2.length());
    
    for (int i = 0; i < maxLen; i++) {
        if (i < word1.length()) sb.append(word1.charAt(i));
        if (i < word2.length()) sb.append(word2.charAt(i));
    }
    
    return sb.toString();
}
```

## 💡 알고리즘 패턴
- **StringBuilder**: 문자열 조작 성능 최적화
- **투포인터**: 두 문자열을 동시 순회

## ⚡ 복잡도 분석
- **시간복잡도**: O(n + m) - n, m은 각 문자열의 길이
- **공간복잡도**: O(n + m) - 결과 문자열 저장

## 🎓 핵심 포인트
- **StringBuilder 사용**: String 직접 연결 시 O(n²)이 되므로 StringBuilder로 최적화
- **경계 체크**: 각 문자열의 길이가 다를 수 있으므로 인덱스 범위 확인
- **charAt() 활용**: 문자열의 특정 위치 문자에 효율적 접근

## 📚 비슷한 문제들
- LeetCode 28: Find the Index of the First Occurrence in a String
- 백준 1152: 단어의 개수 (문자열 파싱)
