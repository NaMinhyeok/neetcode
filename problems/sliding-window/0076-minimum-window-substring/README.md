# 76. Minimum Window Substring

| 항목 | 내용 |
|------|------|
| 난이도 | Hard |
| 카테고리 | Sliding Window |
| NeetCode | [문제 링크](https://neetcode.io/problems/minimum-window-substring) |
| LeetCode | [문제 링크](https://leetcode.com/problems/minimum-window-substring/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=jSto0O4AJbM) |
| Topics | Hash Table, String, Sliding Window |

---

## 문제 설명

Given two strings `s` and `t` of lengths `m` and `n` respectively, return *the **minimum window*** ***substring*** *of* `s` *such that every character in* `t` *(**including duplicates**) is included in the window*. If there is no such substring, return *the empty string* `""`.

The testcases will be generated such that the answer is **unique**.

**Example 1:**

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

**Example 2:**

```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

**Example 3:**

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

**Constraints:**

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 105`
- `s` and `t` consist of uppercase and lowercase English letters.

**Follow up:** Could you find an algorithm that runs in `O(m + n)` time?

---



<details><summary>💡 Hint 1</summary>

Use two pointers to create a window of letters in s, which would have all the characters from t.

</details>


<details><summary>💡 Hint 2</summary>

Expand the right pointer until all the characters of t are covered.

</details>


<details><summary>💡 Hint 3</summary>

Once all the characters are covered, move the left pointer and ensure that all the characters are still covered to minimize the subarray size.

</details>


<details><summary>💡 Hint 4</summary>

Continue expanding the right and left pointers until you reach the end of s.

</details>



