class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> solution;
        map<int,int> mp;
        for(int i=0;i<nums.size();i++){
            if(mp.find(target-nums[i])==mp.end()) mp[nums[i]]=i;
            else{
                solution.push_back(mp[target-nums[i]]);
                solution.push_back(i);
            }
        }
        return solution;
    }
};
