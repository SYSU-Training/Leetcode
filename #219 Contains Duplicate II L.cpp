class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map <int,int> sto;
        int n=nums.size();
        if(n==1||n==0) return false;
        else{
            for(int i=0;i<n;i++){
                if(sto.find(nums[i])!=sto.end()&&i-sto[nums[i]]<=k) 
                return true;
                else sto[nums[i]]=i;
            }
            return false;
        }
    }
};
