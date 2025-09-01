# 01_String 개념 지도

## 🎯 언제 사용하는가?
- 문자열 조작, 변환, 파싱이 필요할 때
- 문자 빈도 계산, 아나그램, 회문 판별 문제
- 패턴 매칭, 부분 문자열 검색 문제
- 입력이 문자열이고 결과도 문자열인 경우

**대표적인 문제 유형들**:
- 문자열 합치기/분리: 두 문자열 교대로 합치기, split 활용
- 문자열 변환: 대소문자 변환, 숫자↔문자 변환
- 문자열 검색: 부분 문자열 찾기, 패턴 매칭
- 회문/아나그램: 투포인터로 대칭 확인, 빈도 비교

## 🧠 사고 과정 (Mental Model)
```
문제 → 문자열 조작 인식 → 성능 고려 → StringBuilder vs String
```

1. **패턴 인식**: 문자열 입출력, 문자 단위 처리가 필요한가?
2. **핵심 아이디어**: 반복적 문자열 연결 → StringBuilder, 문자 비교 → charAt()
3. **구현 선택**: 길이가 짧으면 String, 긴 문자열이나 반복 연결은 StringBuilder

## 🛠️ 핵심 템플릿 코드

### 🔸 StringBuilder 패턴 (가장 자주 사용)
```java
StringBuilder sb = new StringBuilder();
for (int i = 0; i < n; i++) {
    sb.append(char/string);  // O(1) amortized
}
return sb.toString();
```

### 🔸 투포인터 문자열 탐색 (회문, 대칭)
```java
int left = 0, right = s.length() - 1;
while (left < right) {
    if (s.charAt(left) != s.charAt(right)) return false;
    left++; right--;
}
return true;
```

### 🔸 문자 빈도 카운팅 (아나그램, 빈도 비교)
```java
int[] count = new int[26];  // 영문 소문자
for (char c : s.toCharArray()) {
    count[c - 'a']++;
}
```

## ⚠️ 함정 & 실수 방지

### 💥 자주 터지는 실수들
1. **String 직접 연결 (+=)**:
   - 왜 실수하는가: 매번 새 객체 생성으로 O(n²) 시간복잡도
   - 해결 방법: StringBuilder 사용하여 O(n)으로 최적화
   
2. **인덱스 범위 초과**:
   - 왜 실수하는가: charAt(), substring() 사용 시 길이 확인 누락
   - 해결 방법: 항상 i < s.length() 조건 확인

### 🎯 디버깅 체크리스트
- [ ] 빈 문자열 처리 (length() == 0)
- [ ] charAt() 사용 전 인덱스 범위 확인
- [ ] 대소문자 처리 필요한지 확인
- [ ] 공백/특수문자 처리 고려
- [ ] 문자열 비교 시 equals() 사용 (== 금지)

## � 복잡도 분석 가이드

| 구현 방식 | 시간복잡도 | 공간복잡도 | 언제 사용? |
|-----------|------------|------------|------------|
| String += | O(n²) | O(n²) | 절대 사용 금지 |
| StringBuilder | O(n) | O(n) | 문자열 연결 기본 |
| char[] 배열 | O(n) | O(n) | 메모리 최적화 필요시 |

## 📋 학습 로드맵

### 🥉 초급 (패턴 익히기)
- [1768 문자열 교대로 합치기](./notes/1768_merge_strings_alternately.md) - StringBuilder 기본

### 🥈 중급 (최적화 & 응용)  
- [ ] 회문 판별 - 투포인터 활용
- [ ] 아나그램 체크 - 빈도 카운팅

### 🥇 고급 (마스터 레벨)
- [ ] KMP 알고리즘 - 패턴 매칭 최적화
- [ ] 문자열 해싱 - 빠른 부분문자열 비교

## 🔗 연관 패턴 지도

### 🤝 함께 사용되는 패턴들
- **투포인터**: 회문 판별, 부분 문자열 검색
- **해시맵**: 아나그램 체크, 문자 빈도 비교
- **슬라이딩윈도우**: 최소 윈도우 부분 문자열

### 🔀 대안 패턴들  
- **배열로 문자 처리**: char[] 배열이 더 효율적인 경우
- **정규표현식**: 복잡한 패턴 매칭은 regex 고려

## 💡 실전 팁 & 경험담

### 🎪 면접에서 자주 나오는 변형
- "문자열을 뒤집어라" → StringBuilder.reverse() vs 투포인터
- "대소문자 구분 없이" → toLowerCase() 전처리 vs 비교 시 처리

### 🏆 고수들의 노하우
- StringBuilder 초기 용량 설정: `new StringBuilder(expectedSize)`
- 문자열 길이가 작으면 String 연결도 괜찮음 (JVM 최적화)
- char - 'a' 트릭으로 알파벳을 0~25 인덱스로 변환

### 🤔 이런 경우엔 어떻게?
- Q: 유니코드 문자 처리는?
- A: char[] 대신 String.codePoints() 스트림 활용
