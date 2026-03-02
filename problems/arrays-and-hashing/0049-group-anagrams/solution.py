# NeetCode - Arrays & Hashing
# 49. Group Anagrams (Medium)
# https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for s in strs:
            count = [0] * 26  # a to z

            for c in s:
                count[ord(c) - ord("a")] += 1

            maps[tuple(count)].append(s)

        return list(maps.values())
