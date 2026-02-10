# 72. Edit Distance

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | 2-D Dynamic Programming |
| NeetCode | [문제 링크](https://neetcode.io/problems/edit-distance) |
| LeetCode | [문제 링크](https://leetcode.com/problems/edit-distance/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=XYi2-LPrwm4) |
| Topics | String, Dynamic Programming |

---

## 문제 설명

Given two strings `word1` and `word2`, return *the minimum number of operations required to convert `word1` to `word2`*.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

**Example 1:**

```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

**Example 2:**

```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

**Constraints:**

- `0 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of lowercase English letters.

---


