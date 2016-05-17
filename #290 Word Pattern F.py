# same as #205 Isomorphic Strings
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p=list(pattern)
        s=str.split()
        if len(s)!=len(p):
            return False
        p_dic={}
        s_dic={}
        for i in range(len(s)):
            if p[i] in p_dic.keys() and p_dic[p[i]]!=s[i]:
                return False
            if s[i] in s_dic.keys() and s_dic[s[i]]!=p[i]:
                return False
            p_dic[p[i]],s_dic[s[i]]=s[i],p[i]
        return True
            