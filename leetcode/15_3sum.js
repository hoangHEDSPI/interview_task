/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    
    function sortNumber(a,b){
        return a - b;
    }
    let result = [];

    nums.sort(sortNumber);
    // console.log(nums)
    n_length = nums.length;
    if (nums[0] > 0 || n_length < 3) return result;

    for (let i = 0 ; i < n_length-2; i++) {
        if (i == 0 || (i > 0 && nums[i] >= nums[i-1])) {
            // console.log("i = ", i);
            let target = 0 - nums[i];
            // console.log("target = " + target);
            let start = i+1;

            let end = n_length-1;
            while (start < end) {
                
                if (nums[start] + nums[end] == target) {
                    // console.log("nums[start] = " + nums[start]);
                    // console.log("nums[end] = " + nums[end]);
                    result.push([nums[i], nums[start], nums[end]]);
                    while (start < end && nums[start] == nums[start+1])
                        start++;
                    while (start < end && nums[end] == nums[end-1]) 
                        end--;
                    
                   
                    start += 1;
                    end -= 1;
                }
                else if (nums[start] + nums[end] > target) end--;
                else start++;
            }
        }
    }
    return result;
    
};

// Improve this solution by two-pointers based algorithm

var nums = [-1,0,1,2,-1,-4];
console.log(threeSum(nums));
