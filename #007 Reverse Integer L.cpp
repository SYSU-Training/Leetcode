class Solution {
public:
    int reverse(int x) {
        long y=0;
        while(x){
            if (y>(2147483647)/10||y<(-2147483648)/10) return 0;
            long z=x%10;
            y=y*10+z;
            x=x/10;
        }
        return y;
    }
};
