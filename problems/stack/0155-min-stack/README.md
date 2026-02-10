# 155. Min Stack

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | Stack |
| NeetCode | [문제 링크](https://neetcode.io/problems/min-stack) |
| LeetCode | [문제 링크](https://leetcode.com/problems/min-stack/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=qkLl7nAwDPo) |
| Topics | Stack, Design |

---

## 문제 설명

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

**Example 1:**

```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

**Constraints:**

- `-231 <= val <= 231 - 1`
- Methods `pop`, `top` and `getMin` operations will always be called on **non-empty** stacks.
- At most `3 * 104` calls will be made to `push`, `pop`, `top`, and `getMin`.

---



<details><summary>💡 Hint 1</summary>

Consider each node in the stack having a minimum value. (Credits to @aakarshmadhavan)

</details>



