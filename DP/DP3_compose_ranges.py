def composeRanges(nums):
    if nums == []:
        return []
    if len(nums) == 1:
        return [str(nums[0])]
    res_idx = []
    i = 0
    j = 0
    nums.append(0)
    while (i < len(nums)-1):
        if nums[i] != nums[i+1]-1:
            if i == j:
                res_idx.append(str(nums[j]))
            else:
                res_idx.append(str(nums[j]) + "->" + str(nums[i]))
            i += 1
            j = i
        else:
            i += 1
    return res_idx

nums = [1,2]
print (composeRanges(nums))


