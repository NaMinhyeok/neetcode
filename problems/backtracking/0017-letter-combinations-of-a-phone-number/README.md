# 17. Letter Combinations of a Phone Number

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | Backtracking |
| NeetCode | [문제 링크](https://neetcode.io/problems/letter-combinations-of-a-phone-number) |
| LeetCode | [문제 링크](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=0snEunUacZY) |
| Topics | Hash Table, String, Backtracking |

---

## 문제 설명

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)

**Example 1:**

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**Example 2:**

```
Input: digits = "2"
Output: ["a","b","c"]
```

**Constraints:**

- `1 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`.

---


