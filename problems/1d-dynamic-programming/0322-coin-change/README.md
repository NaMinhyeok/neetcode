# 322. Coin Change

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | 1-D Dynamic Programming |
| NeetCode | [문제 링크](https://neetcode.io/problems/coin-change) |
| LeetCode | [문제 링크](https://leetcode.com/problems/coin-change/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=H9bfqozjoqs) |
| Topics | Array, Dynamic Programming, Breadth-First Search |

---

## 문제 설명

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return *the fewest number of coins that you need to make up that amount*. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

**Example 1:**

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

**Example 2:**

```
Input: coins = [2], amount = 3
Output: -1
```

**Example 3:**

```
Input: coins = [1], amount = 0
Output: 0
```

**Constraints:**

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 231 - 1`
- `0 <= amount <= 104`

---


