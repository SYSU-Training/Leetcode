class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        map<int,int> a;
        for(int i=0;i<nums1.size();i++){
        if(a.find(nums1[i])==a.end()) a[nums1[i]]=0;
        }
        vector<int> ic;
        for(int i=0;i<nums2.size();i++){
            if(a.find(nums2[i])!=a.end()){
                ic.push_back(nums2[i]);
                a.erase(nums2[i]);
            }
        }
        return ic;
    }
};
