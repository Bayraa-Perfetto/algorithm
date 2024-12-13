class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashMap; // To store value and its index
        
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            // Check if complement is in the hash map
            if (hashMap.find(complement) != hashMap.end()) {
                return {hashMap[complement], i};
            }
            // Store the current number with its index
            hashMap[nums[i]] = i;
        }
        return {}; // In case no solution exists (not expected in valid inputs)
    }
};
