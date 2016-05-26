#7. Reverse Integer
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y=abs(x)
        z=list(str(y))
        z=z[::-1]
        sum=0
        for i in range(len(z)):
            sum=sum+int(z[i])*10**(len(z)-i-1)
        if sum>(2**31-1):
            return 0
        if x<0:
            return -sum
        return sum