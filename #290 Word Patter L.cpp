class Solution {
public:
    bool wordPattern(string pattern, string str) {
        vector<string> vs;
        map<char,string> map1;
        map<string,char> map2;
        string s="";
        for(int i=0;i<str.size();i++){
            if(str[i]!=' ') s=s+str[i];
            else {
                vs.push_back(s);
                s="";
            }
            if(i==str.size()-1) vs.push_back(s);
        }
        if(pattern.size()!=vs.size()) return false;
        for(int i=0;i<pattern.size();i++){
            if(map1.find(pattern[i])==map1.end()&&map2.find(vs[i])==map2.end()){
                map1.insert(make_pair(pattern[i],vs[i]));
                map2.insert(make_pair(vs[i],pattern[i]));
            }
            else if(map1[pattern[i]]!=vs[i]||map2[vs[i]]!=pattern[i]) return false;
        }
        return true;
    }
};
