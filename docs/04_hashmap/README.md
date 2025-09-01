# 04_HashMap 개념 지도

## 🎯 언제 사용하는가?
- 빈도수 계산이 필요한 경우
- 빠른 검색/존재 여부 확인 (O(1))
- Key-Value 매핑 관계 처리
- 중복 제거나 유니크한 값 추적

**대표적인 문제 유형들**:
- 빈도 카운팅: 문자/숫자 등장 횟수 세기
- 존재 판별: 특정 값이 있는지 빠르게 확인
- 그룹핑: 같은 특성을 가진 데이터 묶기
- 캐싱: 이전 계산 결과 저장 (메모이제이션)

## 🧠 사고 과정 (Mental Model)
```
문제 → 검색/카운팅 필요? → O(1) 접근 필요? → HashMap 선택
```

1. **패턴 인식**: "몇 번 나타나는가?", "존재하는가?", "빠른 검색"
2. **핵심 아이디어**: 배열 O(n) 검색 → HashMap O(1) 검색
3. **구현 선택**: HashMap vs HashSet vs TreeMap (정렬 필요시)

## 🛠️ 핵심 템플릿 코드

### 🔸 빈도 카운팅 패턴 (가장 자주 사용)
```java
HashMap<Character, Integer> count = new HashMap<>();
for (char c : str.toCharArray()) {
    count.put(c, count.getOrDefault(c, 0) + 1);
}
```

### 🔸 존재 여부 확인 (빠른 검색)
```java
HashSet<Integer> seen = new HashSet<>();
for (int num : nums) {
    if (seen.contains(target - num)) {
        return true; // 합이 target인 쌍 발견
    }
    seen.add(num);
}
```

### 🔸 그룹핑/분류 패턴
```java
HashMap<String, List<String>> groups = new HashMap<>();
for (String word : words) {
    String key = getKey(word); // 분류 기준
    groups.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
}
```

## ⚠️ 함정 & 실수 방지

### 💥 자주 터지는 실수들
1. **null 값 처리**:
   - 왜 실수하는가: get() 결과가 null일 수 있음을 간과
   - 해결 방법: getOrDefault() 사용하거나 containsKey() 먼저 확인
   
2. **해시 충돌 고려 부족**:
   - 왜 실수하는가: 최악의 경우 O(n) 성능 가능
   - 해결 방법: 좋은 해시 함수 사용, equals()/hashCode() 올바른 구현

### 🎯 디버깅 체크리스트
- [ ] null key/value 처리 확인
- [ ] get() vs getOrDefault() 적절한 선택
- [ ] 키 타입의 equals()/hashCode() 구현 확인
- [ ] 메모리 사용량 고려 (큰 데이터셋)
- [ ] 동시성 필요시 ConcurrentHashMap 사용

## 📊 복잡도 분석 가이드

| 구현 방식 | 시간복잡도 | 공간복잡도 | 언제 사용? |
|-----------|------------|------------|------------|
| HashMap | O(1) 평균, O(n) 최악 | O(n) | 일반적인 빠른 검색 |
| TreeMap | O(log n) | O(n) | 정렬된 순서 필요시 |
| LinkedHashMap | O(1) | O(n) | 삽입 순서 유지 필요시 |
| HashSet | O(1) 평균 | O(n) | 유니크 값만 필요시 |

## 📋 학습 로드맵

### 🥉 초급 (패턴 익히기)
- 텍스트만 - 기본 매핑

### 🥈 중급 (최적화 & 응용)  
- [ ] Two Sum 문제 - 해시맵으로 O(n) 최적화
- [ ] 아나그램 그룹핑 - 문자열 분류

### 🥇 고급 (마스터 레벨)
- [ ] LRU Cache - LinkedHashMap 활용
- [ ] 일관된 해싱 - 분산 시스템

## 🔗 연관 패턴 지도

### 🤝 함께 사용되는 패턴들
- **문자열**: 문자 빈도 계산, 아나그램 체크
- **배열**: Two Sum, 중복 찾기 최적화
- **그래프**: 인접 리스트 표현
- **DP**: 메모이제이션으로 중복 계산 방지

### 🔀 대안 패턴들  
- **배열**: 키 범위가 작고 연속적일 때 (예: 알파벳 26개)
- **이진탐색**: 정렬된 데이터에서 O(log n) 검색도 충분할 때
- **Trie**: 문자열 prefix 검색이 필요할 때

## 💡 실전 팁 & 경험담

### 🎪 면접에서 자주 나오는 변형
- "배열에서 두 수의 합" → 브루트포스 O(n²) vs 해시맵 O(n)
- "문자열 아나그램" → 정렬 O(n log n) vs 빈도 카운팅 O(n)
- "중복 찾기" → 이중루프 vs HashSet 한번 순회

### 🏆 고수들의 노하우
- `Map.computeIfAbsent()` 활용으로 깔끔한 코드
- 초기 용량 설정: `new HashMap<>(expectedSize * 4/3)`
- Primitive 타입용: `TIntIntHashMap` 같은 라이브러리 고려

### 🤔 이런 경우엔 어떻게?
- Q: 메모리가 부족할 때는?
- A: Bloom Filter로 근사 검색 또는 외부 정렬
- Q: 키가 복잡한 객체일 때는?
- A: equals()/hashCode() 정확히 구현하거나 키를 단순화
