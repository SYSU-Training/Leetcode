class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0) return false;
        int y=1;
        while(x/y>=10) y=y*10;
        while(x){
            int max=x/y;
            int min=x%10;
            if(max!=min) return false;
            else
            {
                x=x-max*y;
                x=x/10;
                y=y/100;
            }
        }
        return true;
    }
};
