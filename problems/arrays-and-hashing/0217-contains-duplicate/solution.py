# NeetCode - Arrays & Hashing
# 217. Contains Duplicate (Easy)
# https://leetcode.com/problems/contains-duplicate/

class Solution:
    # 시간 복잡도 : O(N)
    # 공간 복잡도 : O(N)
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = list(set(nums))

        return len(unique) != len(nums)
