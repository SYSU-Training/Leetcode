#205. Isomorphic Strings

#Method 1
class Solution(object):
    def isIsomorphic(self, a, b):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        da={}   # item_name:a[i];item_value:b[i]
        db={}   # item_name:b[i];item_value:a[i]
        for t in range(len(a)):
            aa,bb=da.get(a[t]),db.get(b[t])
            if aa==None and bb==None:
                da[a[t]]=b[t]
                db[b[t]]=a[t]
            elif aa!=b[t] or bb!=a[t]:
                return False
        return True


#Method 2       
'''
longer code, shorter time
'''
class Solution(object):
    def isIsomorphic(self, a, b):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #if a==b:
        #    return True
        d={}
        for i,v in enumerate(a):
            if v in d:
                if b[i]!=b[d[v]]:
                    return False
            else:
                d[v]=i
        d={}
        for i,v in enumerate(b):
            if v in d:
                if a[i]!=a[d[v]]:
                    return False
            else:
                d[v]=i
        return True

'''
shorter code, longer time
'''
class Solution(object):
    def isIsomorphic(self, a, b):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
       
        #if a==b:
        #    return True 
        c=[a,b]
        for j in range(len(c)):
            d={}
            for i,v in enumerate(c[j]):
                if v in d:
                    if c[1-j][i]!=c[1-j][d[v]]:
                        return False
                else:
                    d[v]=i
                
        return True


#Method 1+
'''
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        sourceMap, targetMap = dict(), dict()
        for x in range(len(s)):
            source, target = sourceMap.get(t[x]), targetMap.get(s[x])
            if source is None and target is None:
                sourceMap[t[x]], targetMap[s[x]] = s[x], t[x]
            elif target != t[x] or source != s[x]:
                return False
        return True
'''

'''
def isIsomorphic(s, t):
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        if s[i] in s_dict.keys() and s_dict[s[i]] != t[i]:
            return False
        if t[i] in t_dict.keys() and t_dict[t[i]] != s[i]:
            return False
        s_dict[s[i]] = t[i]
        t_dict[t[i]] = s[i]
    return True
'''
