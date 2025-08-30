# 06_Sorting_Searching 개념 지도

## 🎯 언제 사용하는가?
- 데이터를 순서대로 정렬해야 하는 경우
- 정렬된 데이터에서 빠른 검색이 필요한 경우
- K번째 원소, 순위 관련 문제
- 최적화 문제에서 파라미터 서치가 필요한 경우

**대표적인 문제 유형들**:
- 기본 정렬: 오름차순, 내림차순, 커스텀 비교
- 이진 탐색: 특정 값 찾기, Lower/Upper Bound
- K번째 원소: QuickSelect, 힙 활용
- 파라미터 서치: 이진 탐색으로 최적값 찾기

## 🧠 사고 과정 (Mental Model)
```
문제 → 정렬 필요? → 탐색 필요? → 정렬 알고리즘 vs 이진탐색 선택
```

1. **패턴 인식**: "정렬하라", "K번째", "범위 내 개수" 등의 키워드
2. **핵심 아이디어**: 정렬 O(n log n), 이진탐색 O(log n)
3. **구현 선택**: Arrays.sort() vs 직접 구현, 일반 vs 파라미터 서치

## 🛠️ 핵심 템플릿 코드

### 🔸 기본 정렬 패턴 (가장 자주 사용)
```java
// 오름차순
Arrays.sort(arr);

// 커스텀 비교 (내림차순)
Arrays.sort(arr, Collections.reverseOrder());

// 객체 정렬
Arrays.sort(students, (a, b) -> a.score - b.score);
```

### 🔸 이진 탐색 (Binary Search)
```java
// 기본 이진 탐색
int left = 0, right = arr.length - 1;
while (left <= right) {
    int mid = left + (right - left) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
}
return -1; // 찾지 못함
```

### 🔸 파라미터 서치 (최적화 문제)
```java
// 조건을 만족하는 최소값 찾기
int left = minValue, right = maxValue;
while (left < right) {
    int mid = left + (right - left) / 2;
    if (canSolve(mid)) {
        right = mid; // 가능하면 더 작은 값 시도
    } else {
        left = mid + 1; // 불가능하면 더 큰 값 필요
    }
}
return left;
```

## ⚠️ 함정 & 실수 방지

### 💥 자주 터지는 실수들
1. **중간값 오버플로우**:
   - 왜 실수하는가: `(left + right) / 2`에서 오버플로우
   - 해결 방법: `left + (right - left) / 2` 사용
   
2. **무한 루프**:
   - 왜 실수하는가: `left < right` vs `left <= right` 혼동
   - 해결 방법: 찾는 값 vs 범위에 따라 조건 정확히 설정

### 🎯 디버깅 체크리스트
- [ ] 배열이 정렬되어 있는지 확인 (이진탐색 전제조건)
- [ ] 중간값 계산 오버플로우 방지
- [ ] 루프 종료 조건 정확한지 확인
- [ ] 경계값 처리 (빈 배열, 크기 1)
- [ ] Comparator 일관성 확인

## 📊 복잡도 분석 가이드

| 구현 방식 | 시간복잡도 | 공간복잡도 | 언제 사용? |
|-----------|------------|------------|------------|
| Arrays.sort() | O(n log n) | O(log n) | 일반적인 정렬 |
| 이진 탐색 | O(log n) | O(1) | 정렬된 배열 검색 |
| QuickSelect | O(n) 평균 | O(1) | K번째 원소 |
| 카운팅 정렬 | O(n + k) | O(k) | 작은 정수 범위 |

## 📋 학습 로드맵

### 🥉 초급 (패턴 익히기)
- [x] [2587 대표값2](./notes/2587_representative_value.md) - 기본 정렬과 중앙값
- [x] [2705 수 정렬하기](./notes/2705_number_sort.md) - 기본 정렬
- [x] [25305 커트라인](./notes/25305_cutline.md) - K번째 원소

### 🥈 중급 (최적화 & 응용)  
- [x] [2751 수 정렬하기 2](./notes/2751_number_sort_2.md) - 대용량 정렬
- [x] [10989 수 정렬하기 3](./notes/10989_number_sort_3.md) - 메모리 최적화
- [x] [실패율](./notes/failure_rate.md) - 커스텀 정렬

### 🥇 고급 (마스터 레벨)
- [ ] 이진 탐색 응용 - Lower/Upper Bound
- [ ] 파라미터 서치 - 최적화 문제

## 🔗 연관 패턴 지도

### 🤝 함께 사용되는 패턴들
- **투포인터**: 정렬 후 두 포인터로 효율적 탐색
- **해시맵**: 정렬 전 빈도 계산
- **그리디**: 정렬 후 최적 선택
- **분할정복**: 머지소트, 퀵소트의 기본 원리

### 🔀 대안 패턴들  
- **우선순위큐**: K번째 원소를 계속 추적해야 할 때
- **계수정렬**: 정수 범위가 작을 때 O(n) 정렬
- **해시맵**: 정렬 없이 빠른 검색만 필요할 때

## 💡 실전 팁 & 경험담

### 🎪 면접에서 자주 나오는 변형
- "K번째로 큰 수" → QuickSelect vs 힙 vs 정렬
- "두 배열 합쳐서 정렬" → 병합 vs 단순 합치기 후 정렬
- "범위 내 개수" → 이진탐색으로 Upper - Lower

### 🏆 고수들의 노하우
- Java `Arrays.sort()`는 primitive는 퀵소트, 객체는 머지소트
- `Collections.binarySearch()` 활용으로 구현 간소화
- Comparator 체이닝: `.thenComparing()` 으로 다중 정렬 기준

### 🤔 이런 경우엔 어떻게?
- Q: 안정 정렬이 필요할 때는?
- A: 객체 배열로 변환하거나 병합정렬 직접 구현
- Q: 부분 정렬만 필요할 때는?
- A: PriorityQueue나 QuickSelect 활용
