class Solution {
public:
    
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        unordered_map<int, int> hash;
        
        for (int i = 0; i < nums.size(); i++) {
            int z = target - nums[i];
            if (hash.find(z) != hash.end()) {
                result.push_back(hash[z]);
                result.push_back(i);
                return result;
            }
            else
                hash[nums[i]] = i;
        }
        return result;
    }
};
