# 763. Partition Labels

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | Greedy |
| NeetCode | [문제 링크](https://neetcode.io/problems/partition-labels) |
| LeetCode | [문제 링크](https://leetcode.com/problems/partition-labels/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=B7m8UmZE-vw) |
| Topics | Hash Table, Two Pointers, String, Greedy |

---

## 문제 설명

You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string `"ababcc"` can be partitioned into `["abab", "cc"]`, but partitions such as `["aba", "bcc"]` or `["ab", "ab", "cc"]` are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`.

Return *a list of integers representing the size of these parts*.

**Example 1:**

```
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
```

**Example 2:**

```
Input: s = "eccbbbbdec"
Output: [10]
```

**Constraints:**

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

---



<details><summary>💡 Hint 1</summary>

Try to greedily choose the smallest partition that includes the first letter.  If you have something like "abaccbdeffed", then you might need to add b.  You can use an map like "last['b'] = 5" to help you expand the width of your partition.

</details>



