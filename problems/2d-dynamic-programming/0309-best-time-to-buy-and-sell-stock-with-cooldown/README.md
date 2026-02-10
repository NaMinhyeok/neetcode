# 309. Best Time to Buy And Sell Stock With Cooldown

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | 2-D Dynamic Programming |
| NeetCode | [문제 링크](https://neetcode.io/problems/best-time-to-buy-and-sell-stock-with-cooldown) |
| LeetCode | [문제 링크](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=I7j0F7AHpb8) |
| Topics | Array, Dynamic Programming |

---

## 문제 설명

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

**Example 1:**

```
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```

**Example 2:**

```
Input: prices = [1]
Output: 0
```

**Constraints:**

- `1 <= prices.length <= 5000`
- `0 <= prices[i] <= 1000`

---


