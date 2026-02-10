# 3. Longest Substring Without Repeating Characters

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | Sliding Window |
| NeetCode | [문제 링크](https://neetcode.io/problems/longest-substring-without-repeating-characters) |
| LeetCode | [문제 링크](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=wiGpQwVHdE0) |
| Topics | Hash Table, String, Sliding Window |

---

## 문제 설명

Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

**Example 1:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
```

**Example 2:**

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Constraints:**

- `0 <= s.length <= 5 * 104`
- `s` consists of English letters, digits, symbols and spaces.

---



<details><summary>💡 Hint 1</summary>

Generate all possible substrings & check for each substring if it's valid and keep updating maxLen accordingly.

</details>



