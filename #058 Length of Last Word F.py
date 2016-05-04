#58. Length of Last Word

'''
Method1
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length=0
        length2=0
        for i in range(len(s)):
            if s[i]==" ":
                length=0
            else:
                length=length+1
                length2=length
        return length if length!=0 else length2

'''
Method2
http://blog.csdn.net/hyperbolechi/article/details/43469491
'''
class Solution:  
    # @param s, a string  
    # @return an integer  
    def lengthOfLastWord(self, s):  
        s=s.split()  #str.split() seperate words
        if not s:  # if s!=""
            return 0  
        else:  
            return len(s[-1])  