from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def construct(nums: List[int], l:int, r:int):
            if l == r:
                return None
            i = nums[l:r].index(max(nums[l:r]))
            root = TreeNode(nums[i])
            root.left = construct(nums, l, i-1)
            root.right = construct(nums, i+1, r)
            return root
        return construct(nums, 0, len(nums))


if __name__ == '__main__':
    nums = [3,2,1,6,0,5]
    sol = Solution()
    sol.constructMaximumBinaryTree(nums)