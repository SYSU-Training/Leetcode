#171 Excel Sheet Column Number

#Method 2.1
#Recursive
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==1:
            return ord(s)-64
        return ord(s[-1])-64+26*self.titleToNumber(s[:-1])

#Method 2.2
#Iterative
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        n=len(s)
        for i in range(n):
            res=res*26+ord(s[i])-64
        return res

#Method 1 -->my code
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=map(chr,range(65,91))  #65-97 ->A-Z ASCII; 97-123 ->a-z
        b=range(1,27)
        d={}
        for i in range(26):
            d[a[i]]=b[i]
        sum=0
        for i in range(len(s)):
            sum=sum+d[s[len(s)-i-1]]*(26**i)
        return sum