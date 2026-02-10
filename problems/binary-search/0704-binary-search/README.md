# 704. Binary Search

| 항목 | 내용 |
|------|------|
| 난이도 | Easy |
| 카테고리 | Binary Search |
| NeetCode | [문제 링크](https://neetcode.io/problems/binary-search) |
| LeetCode | [문제 링크](https://leetcode.com/problems/binary-search/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=s4DPM8ct1pI) |
| Topics | Array, Binary Search |

---

## 문제 설명

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

**Example 2:**

```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```

**Constraints:**

- `1 <= nums.length <= 104`
- `-104 < nums[i], target < 104`
- All the integers in `nums` are **unique**.
- `nums` is sorted in ascending order.

---


