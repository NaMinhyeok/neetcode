# NeetCode - Two Pointers
# 125. Valid Palindrome (Easy)
# https://leetcode.com/problems/valid-palindrome/

class Solution:
    # 시간복잡도: O(N)
    # 공간복잡도: O(N)
    def isPalindrome(self, s: str) -> bool:
        result = re.sub(r'[^a-zA-Z0-9]','',s).strip().replace(" ", "").lower()
        candidates = list(result)
        center = len(result)//2
        if len(result) % 2 == 0:
            forward = candidates[:center]
            backward = candidates[center:]
            print(f"forward: {forward}")
            print(f"backward: {backward}")
            return forward == backward[::-1]
        else:
            forward = candidates[:center]
            backward = candidates[center+1:]
            print(f"forward: {forward}")
            print(f"backward: {backward}")
            return forward == backward[::-1]
