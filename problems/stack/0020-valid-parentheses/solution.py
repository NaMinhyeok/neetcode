# NeetCode - Stack
# 20. Valid Parentheses (Easy)
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        # 스택이 빌때까지 {[( <- 는 push )]}
        if s[0] == '}' or s[0] == ']' or s[0] == ')':
            return False
        for val in s:
            if val == '{' or val == '[' or val == '(':
                stack.append(val)
            else:
                if len(stack) == 0:
                    return False
                if val == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                elif val == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif val == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0

