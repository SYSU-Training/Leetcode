class Solution {
public:
    int getSum(int a, int b) {
        int k1=a^b;
        int k2=(a&b)<<1;
        if(k2!=0){
            k1=getSum(k1,k2);
        }
        return k1;
    }
};
