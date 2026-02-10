# 70. Climbing Stairs

| 항목 | 내용 |
|------|------|
| 난이도 | Easy |
| 카테고리 | 1-D Dynamic Programming |
| NeetCode | [문제 링크](https://neetcode.io/problems/climbing-stairs) |
| LeetCode | [문제 링크](https://leetcode.com/problems/climbing-stairs/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=Y0lT9Fck7qI) |
| Topics | Math, Dynamic Programming, Memoization |

---

## 문제 설명

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Example 1:**

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2:**

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

**Constraints:**

- `1 <= n <= 45`

---



<details><summary>💡 Hint 1</summary>

To reach nth step, what could have been your previous steps? (Think about the step sizes)

</details>



