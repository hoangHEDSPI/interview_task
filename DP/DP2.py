def houseRobber(nums):
    if nums is None: return 0
    if len(nums) == 1: return nums[0]
    S = [0 for i in range(len(nums))]
    S[0] = nums[0]
    S[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        S[i] = max(S[i-1], S[i-2]+nums[i])
    return S[len(nums)-1]

nums = []
print houseRobber(nums)