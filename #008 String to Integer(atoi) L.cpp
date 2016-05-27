class Solution {
public:
    int myAtoi(string str) {
        int k=str.size();
        int i=0;
        long long a=0;
        int mark=0;
        int mark2=0;
        int mark3=0;
        int b=0;
        for(i=1;i<=k;i++){
            if(str[i-1]==' '&&mark3==0&&mark2==0&&mark==0) {continue;}
            if(str[i-1]=='+'&&mark3==0&&mark2==0&&mark==0) {mark2=1;continue;}
            if(str[i-1]=='-'&&mark3==0&&mark2==0&&mark==0) {mark=1;continue;}
            if(str[i-1]<='9'&&str[i-1]>='0') {mark3=1;b=str[i-1]-'0';}
            if(str[i-1]>'9'||str[i-1]<'0') break;
            a=a*10+b;
            if(a>2147483647&&mark!=1) return 2147483647;
            if(a>=2147483648&&mark==1) return -2147483648;
        }
        if(mark2==1&&mark==1) return 0;
        if(mark==1) a=-a;
        return a;
    }
};
