class Solution {
public:
    int mySqrt(int x) {
        double a=1,b=1;
        double e=1;
        while(e>0.000001){
            b=0.5*(a+x/a);
            e=abs(a-b);
            a=b;
        }
        return b;
    }
};
