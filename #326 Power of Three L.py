class Solution(object):
    def isPowerOfThree(self, n):
        if n<1:
            return False
        a=math.log10(n)/math.log10(3)
        k=a-int(a)
        return(abs(k)<10e-15)
