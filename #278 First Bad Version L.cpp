// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int first=1,last=n;
        while(first<last){
            int m=first+(last-first)/2;
            if(isBadVersion(m)){
                last=m;
            }
            else first=m+1;
        }
        return first;
    }
};
