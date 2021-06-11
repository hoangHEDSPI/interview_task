# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack, i = [], 0
        while i < len(S):
            level, val = 0, ""
            while i < len(S) and S[i] == '-':
                level,  i = level + 1, i + 1
            while i < len(S) and S[i] != '-':
                val, i = val + S[i], i + 1
            while len(stack) > level:
                stack.pop()
            node = TreeNode(val)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]


if __name__ == '__main__':
    S = "1-2--3--4-5--6--7"
    sol = Solution()
    sol.recoverFromPreorder(S)

