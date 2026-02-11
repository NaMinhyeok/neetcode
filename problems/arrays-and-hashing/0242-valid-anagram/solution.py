# NeetCode - Arrays & Hashing
# 242. Valid Anagram (Easy)
# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = dict()
        tDict = dict()
        for val in s:
            if val in sDict:
                sDict[val] += 1
            else:
                sDict[val] = 1

        for val in t:
            if val in tDict:
                tDict[val] += 1
            else:
                tDict[val] = 1

        return sDict == tDict
