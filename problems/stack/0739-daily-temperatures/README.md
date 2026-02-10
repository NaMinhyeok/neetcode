# 739. Daily Temperatures

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | Stack |
| NeetCode | [문제 링크](https://neetcode.io/problems/daily-temperatures) |
| LeetCode | [문제 링크](https://leetcode.com/problems/daily-temperatures/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=cTBiBSnjO3c) |
| Topics | Array, Stack, Monotonic Stack |

---

## 문제 설명

Given an array of integers `temperatures` represents the daily temperatures, return *an array* `answer` *such that* `answer[i]` *is the number of days you have to wait after the* `ith` *day to get a warmer temperature*. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

**Example 1:**

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Example 2:**

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

**Example 3:**

```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

**Constraints:**

- `1 <= temperatures.length <= 105`
- `30 <= temperatures[i] <= 100`

---



<details><summary>💡 Hint 1</summary>

If the temperature is say, 70 today, then in the future a warmer temperature must be either 71, 72, 73, ..., 99, or 100.  We could remember when all of them occur next.

</details>



