# 069 Sqrt(x)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:
        	return x

        left=1
        right=x/2

        while left<=right:
        	mid=(left+right)/2
        	if (x>mid*mid):
        		left=left+1
        		lastmid=mid
        	elif (x<mid*mid):
        		right=right+1
        	else: 
        		return mid

        return lastmid


#
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        ans = float(x)
        while True:
            tmp = ans
            ans = (ans + x / ans) / 2
            if abs(ans - tmp) < 1:
                break
        return int(ans)