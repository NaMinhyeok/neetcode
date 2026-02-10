# 33. Search In Rotated Sorted Array

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | Binary Search |
| NeetCode | [문제 링크](https://neetcode.io/problems/search-in-rotated-sorted-array) |
| LeetCode | [문제 링크](https://leetcode.com/problems/search-in-rotated-sorted-array/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=U8XENwh8Oy8) |
| Topics | Array, Binary Search |

---

## 문제 설명

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly left rotated** at an unknown index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be left rotated by `3` indices and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of* `target` *if it is in* `nums`*, or* `-1` *if it is not in* `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2:**

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Example 3:**

```
Input: nums = [1], target = 0
Output: -1
```

**Constraints:**

- `1 <= nums.length <= 5000`
- `-104 <= nums[i] <= 104`
- All values of `nums` are **unique**.
- `nums` is an ascending array that is possibly rotated.
- `-104 <= target <= 104`

---


