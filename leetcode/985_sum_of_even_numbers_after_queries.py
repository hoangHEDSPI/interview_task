class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        first_sum = 0
        res = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                first_sum += nums[i]
        # do queries
        for i in range(len(queries)):
            if (nums[queries[i][1]] + queries[i][0]) % 2 == 0:
                if nums[queries[i][1]] % 2 == 0:
                    first_sum += queries[i][0]
                else:
                    first_sum += nums[queries[i][1]] + queries[i][0]
            else:
                if nums[queries[i][1]] % 2 == 0:
                    first_sum -= nums[queries[i][1]]
            nums[queries[i][1]] += queries[i][0]
            res.append(first_sum)
        
        return res
      
