# 139. Word Break

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | 1-D Dynamic Programming |
| NeetCode | [문제 링크](https://neetcode.io/problems/word-break) |
| LeetCode | [문제 링크](https://leetcode.com/problems/word-break/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=Sx9NNgInc3A) |
| Topics | Array, Hash Table, String, Dynamic Programming, Trie, Memoization |

---

## 문제 설명

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.

**Example 1:**

```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

**Example 2:**

```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
```

**Example 3:**

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

**Constraints:**

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are **unique**.

---


