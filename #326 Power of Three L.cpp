class Solution {
public:
    bool isPowerOfThree(int n) {
        double k;
        if (n==0) return false;
        if (abs((log10(n)/log10(3))-(int)(log10(n)/log10(3)))==0) return true;
        else return false;
}
    };
