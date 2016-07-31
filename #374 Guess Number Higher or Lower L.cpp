// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int k1=1;
        int k2=n;
        while(k1<=k2){
            int mid=k1+(k2-k1)/2;
            int result=guess(mid);
            if(result==0) return mid;
            else if(result==1) k1=mid+1;
            else k2=mid-1;
        }
        return -1;
    }
};
