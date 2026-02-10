# 49. Group Anagrams

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | Arrays & Hashing |
| NeetCode | [문제 링크](https://neetcode.io/problems/group-anagrams) |
| LeetCode | [문제 링크](https://leetcode.com/problems/group-anagrams/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=vzdNOK2oB2E) |
| Topics | Array, Hash Table, String, Sorting |

---

## 문제 설명

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

**Example 1:**

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]

**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

**Explanation:**

- There is no string in strs that can be rearranged to form `"bat"`.
- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.
- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

**Example 2:**

**Input:** strs = [""]

**Output:** [[""]]

**Example 3:**

**Input:** strs = ["a"]

**Output:** [["a"]]

**Constraints:**

- `1 <= strs.length <= 104`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

---


