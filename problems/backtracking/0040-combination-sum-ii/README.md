# 40. Combination Sum II

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | Backtracking |
| NeetCode | [문제 링크](https://neetcode.io/problems/combination-sum-ii) |
| LeetCode | [문제 링크](https://leetcode.com/problems/combination-sum-ii/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=rSA3t6BDDwg) |
| Topics | Array, Backtracking |

---

## 문제 설명

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

**Example 2:**

```
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
```

**Constraints:**

- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

---


