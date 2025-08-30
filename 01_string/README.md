# 01_문자열 패턴

## 🎯 언제 사용하는가?
- 문자열 조작이 필요한 경우 (뒤집기, 합치기, 변환)
- 문자열 파싱/토큰화가 필요한 경우
- 문자열 검색/매칭 패턴 문제
- 아나그램, 회문(팰린드롬) 판별
- 문자 빈도수 계산

## 🛠️ 핵심 템플릿 코드

### StringBuilder 활용 (성능 최적화)
```java
StringBuilder sb = new StringBuilder();
for (int i = 0; i < n; i++) {
    sb.append(char/string);  // O(1) amortized
}
return sb.toString();
```

### 문자열 탐색 (Two Pointer)
```java
int left = 0, right = s.length() - 1;
while (left < right) {
    if (s.charAt(left) != s.charAt(right)) return false;
    left++; right--;
}
```

### 문자 빈도수 카운팅
```java
int[] count = new int[26];  // 영문 소문자
for (char c : s.toCharArray()) {
    count[c - 'a']++;
}
```

## ⚠️ 자주 터지는 실수/주의 포인트

1. **String 직접 연결**: `str += char` 대신 StringBuilder 사용 (O(n²) → O(n))
2. **인덱스 범위 체크**: `charAt()` 사용 시 길이 확인 필수
3. **대소문자 처리**: `toLowerCase()` 또는 `toUpperCase()` 적절히 사용
4. **공백/특수문자**: 입력에 공백이나 특수문자가 포함될 수 있음
5. **문자열 비교**: `==` 대신 `equals()` 사용

## 📋 대표 문제 목록

- [1768_문자열_교대로_합치기](./1768_문자열_교대로_합치기.md) - LeetCode, StringBuilder 기본

## 🔗 연관 문제 (다른 패턴)

- **투포인터**: 회문 판별, 부분 문자열 검색
- **해시맵**: 아나그램 체크, 문자 빈도 비교
- **슬라이딩윈도우**: 최소 윈도우 부분 문자열
