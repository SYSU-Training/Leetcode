class Solution {
public:
    int lengthOfLastWord(string s) {
        if(s.length()==0) return 0;
        if(s.find(' ')==string::npos) return s.length();
        else{
            int len=0;
            for(int i=s.length()-1;i>=0;i--){
                if(s[i]!=' ') len++;
                if(len!=0&&s[i]==' ') return len;
            }
            return len;
        }
    }
};
