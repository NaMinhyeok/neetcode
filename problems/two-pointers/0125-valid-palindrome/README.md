# 125. Valid Palindrome

| 항목 | 내용 |
|------|------|
| 난이도 | Easy |
| 카테고리 | Two Pointers |
| NeetCode | [문제 링크](https://neetcode.io/problems/valid-palindrome) |
| LeetCode | [문제 링크](https://leetcode.com/problems/valid-palindrome/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=jJXJ16kPFWg) |
| Topics | Two Pointers, String |

---

## 문제 설명

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a **palindrome**, or* `false` *otherwise*.

**Example 1:**

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

**Example 2:**

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

**Example 3:**

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

**Constraints:**

- `1 <= s.length <= 2 * 105`
- `s` consists only of printable ASCII characters.

---


