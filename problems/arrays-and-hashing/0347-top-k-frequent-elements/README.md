# 347. Top K Frequent Elements

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | Arrays & Hashing |
| NeetCode | [문제 링크](https://neetcode.io/problems/top-k-frequent-elements) |
| LeetCode | [문제 링크](https://leetcode.com/problems/top-k-frequent-elements/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=YPTqKIgVk-k) |
| Topics | Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect |

---

## 문제 설명

Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

**Example 1:**

**Input:** nums = [1,1,1,2,2,3], k = 2

**Output:** [1,2]

**Example 2:**

**Input:** nums = [1], k = 1

**Output:** [1]

**Example 3:**

**Input:** nums = [1,2,1,2,1,2,3,1,3,2], k = 2

**Output:** [1,2]

**Constraints:**

- `1 <= nums.length <= 105`
- `-104 <= nums[i] <= 104`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

---


