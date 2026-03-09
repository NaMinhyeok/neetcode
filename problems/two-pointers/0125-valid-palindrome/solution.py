# NeetCode - Two Pointers
# 125. Valid Palindrome (Easy)
# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        return newStr == newStr[::-1]
