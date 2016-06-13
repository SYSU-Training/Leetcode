class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        vector<int>::iterator it=nums.begin();
        map<int,int> m;
        while(it!=nums.end()){
            if(m.find(*it)==m.end()){
                m[*it]=*it;
                it++;
            }
            else it=nums.erase(it);
        }
        return nums.size();
    }
};
