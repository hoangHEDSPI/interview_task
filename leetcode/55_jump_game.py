class Solution:
    def canJump(self, nums) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
                print(goal)
        return not goal


if __name__=="__main__":
    nums = [3,2,1,1,4]
    solution = Solution()
    solution.canJump(nums)