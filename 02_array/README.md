# 02_Array 개념 지도

## 🎯 언제 사용하는가?
- 순서가 있는 데이터 집합 처리
- 인덱스 기반 접근이 필요한 경우
- 구간합, 누적합 계산 문제
- 정렬, 탐색이 핵심인 문제

**대표적인 문제 유형들**:
- 배열 순회: 단순 합계, 최대/최소값 찾기
- 구간 처리: 부분 배열의 합, Kadane's algorithm
- 배열 조작: 회전, 뒤집기, 중복 제거
- 이진 탐색: 정렬된 배열에서 빠른 검색

## 🧠 사고 과정 (Mental Model)
```
문제 → 배열 크기/범위 확인 → 순회 vs 구간 vs 탐색 → 알고리즘 선택
```

1. **패턴 인식**: 순서가 중요한가? 인덱스 접근이 필요한가?
2. **핵심 아이디어**: 선형 탐색 O(n), 이진 탐색 O(log n), 구간합 전처리
3. **구현 선택**: 단순 순회 vs 투포인터 vs 슬라이딩 윈도우

## 🛠️ 핵심 템플릿 코드

### 🔸 기본 순회 패턴 (가장 자주 사용)
```java
int sum = 0, max = Integer.MIN_VALUE;
for (int i = 0; i < arr.length; i++) {
    sum += arr[i];
    max = Math.max(max, arr[i]);
}
```

### 🔸 구간합/누적합 (Prefix Sum)
```java
int[] prefixSum = new int[n + 1];
for (int i = 0; i < n; i++) {
    prefixSum[i + 1] = prefixSum[i] + arr[i];
}
// 구간 [i, j] 합: prefixSum[j+1] - prefixSum[i]
```

### 🔸 Kadane's Algorithm (최대 부분합)
```java
int maxSum = arr[0], currentSum = arr[0];
for (int i = 1; i < arr.length; i++) {
    currentSum = Math.max(arr[i], currentSum + arr[i]);
    maxSum = Math.max(maxSum, currentSum);
}
```

## ⚠️ 함정 & 실수 방지

### 💥 자주 터지는 실수들
1. **배열 범위 초과**:
   - 왜 실수하는가: for문에서 <= 사용하거나 length 혼동
   - 해결 방법: i < arr.length 명확히 기억, IDE 경고 확인
   
2. **빈 배열 처리**:
   - 왜 실수하는가: length가 0인 경우 고려 누락
   - 해결 방법: 함수 시작에서 예외 처리

### 🎯 디버깅 체크리스트
- [ ] 배열이 null인지 확인
- [ ] 빈 배열 (length == 0) 처리
- [ ] 인덱스 범위 (0 ≤ i < length)
- [ ] 정수 오버플로우 (큰 수 합계)
- [ ] 음수 값 처리 고려

## 📊 복잡도 분석 가이드

| 구현 방식 | 시간복잡도 | 공간복잡도 | 언제 사용? |
|-----------|------------|------------|------------|
| 선형 탐색 | O(n) | O(1) | 일반적인 순회 |
| 이진 탐색 | O(log n) | O(1) | 정렬된 배열 검색 |
| 구간합 전처리 | O(n) | O(n) | 구간 쿼리 많을 때 |
| 투포인터 | O(n) | O(1) | 두 포인터로 효율적 탐색 |

## 📋 학습 로드맵

### 🥉 초급 (패턴 익히기)
- [x] [내적](./notes/dot_product.md) - 기본 배열 순회
- [x] [두 개 뽑아서 더하기](./notes/pick_two_add.md) - 이중 루프
- [x] [없는 숫자 더하기](./notes/missing_numbers_sum.md) - 수학적 최적화
- [x] [음양 더하기](./notes/add_with_signs.md) - 조건부 처리

### 🥈 중급 (최적화 & 응용)  
- [ ] 구간합 구하기 - Prefix Sum 활용
- [ ] 최대 부분합 - Kadane's Algorithm

### 🥇 고급 (마스터 레벨)
- [ ] 이진 탐색 변형 - Lower/Upper Bound
- [ ] 슬라이딩 윈도우 최적화

## 🔗 연관 패턴 지도

### 🤝 함께 사용되는 패턴들
- **투포인터**: 정렬된 배열에서 두 수의 합
- **이진탐색**: 정렬된 배열에서 빠른 검색
- **해시맵**: 배열 원소의 빈도 계산
- **슬라이딩윈도우**: 고정 크기 구간의 최적값

### 🔀 대안 패턴들  
- **ArrayList**: 크기가 동적으로 변하는 경우
- **Set**: 중복 제거가 필요한 경우
- **PriorityQueue**: 최대/최소값을 계속 추적해야 하는 경우

## 💡 실전 팁 & 경험담

### 🎪 면접에서 자주 나오는 변형
- "배열에서 두 수의 합이 target인 쌍 찾기" → 해시맵 vs 투포인터
- "배열 회전" → 임시 배열 vs 3단계 뒤집기
- "중복 제거" → Set 활용 vs 투포인터

### 🏆 고수들의 노하우
- `Integer.MAX_VALUE/MIN_VALUE` 보다는 실제 데이터 범위 고려
- `Arrays.sort()`, `Collections.sort()` 시간복잡도: O(n log n)
- Stream API: `IntStream.of(arr).sum()` 등 활용

### 🤔 이런 경우엔 어떻게?
- Q: 배열이 너무 커서 메모리 초과가 날 때?
- A: 스트리밍 처리하거나 구간별로 나누어 처리
