class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n=nums.size();
        k=k%n;
        int a[n-1];
        for(int i=0;i<k;i++){
            a[i]=nums[n-k+i];
        }
        for(int i=0;i<n-k;i++){
            a[k+i]=nums[i];
        }
        for(int i=0;i<n;i++){
            nums[i]=a[i];
        }
    }
};
