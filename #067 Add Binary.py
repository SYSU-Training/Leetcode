#67 Add Binary F
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        c='0'+str(int(a)+int(b))
        for i in range(len(c)):
            if c[len(c)-i-1]=='3':
                c=c[:len(c)-i-2]+str(int(c[len(c)-i-2])+1)+'1'+c[len(c)-i:]
            elif c[len(c)-i-1]=='2':
                c=c[:len(c)-i-2]+str(int(c[len(c)-i-2])+1)+'0'+c[len(c)-i:]
        return c if c[0]!='0' else c[1:]
        
