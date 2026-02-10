# 115. Distinct Subsequences

| 항목 | 내용 |
|------|------|
| 난이도 | Hard |
| 카테고리 | 2-D Dynamic Programming |
| NeetCode | [문제 링크](https://neetcode.io/problems/distinct-subsequences) |
| LeetCode | [문제 링크](https://leetcode.com/problems/distinct-subsequences/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=-RDzMJ33nx8) |
| Topics | String, Dynamic Programming |

---

## 문제 설명

Given two strings s and t, return *the number of distinct* ***subsequences*** *of* s *which equals* t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

**Example 1:**

```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
```

**Example 2:**

```
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
```

**Constraints:**

- `1 <= s.length, t.length <= 1000`
- `s` and `t` consist of English letters.

---


