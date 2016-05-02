class Solution(object):
    def isPowerOfFour(self, num):
        if num<=0:
            return False
        import math
        return abs(math.log(num)/math.log(4)-(int)(math.log(num)/math.log(4)))==0
        
