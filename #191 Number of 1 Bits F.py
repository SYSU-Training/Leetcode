#191. Number of 1 Bits   
'''
Hamming weight
'''
#Method 3 
#<-Method 1 & 1+
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        res=0
        while n>0:
            res+=n&1  #n&1 -> if n=0: n&1=0; else n&1=1
            n>>=1     #[n>>=1  -> n=n>>1  #"a>>b" -> a divided by 2 for b times ]<=> [n=int(n/2)]
        return res

# Method 2
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n>=2**32-1): 
            return 32
        else:
            a=bin(n)[2:].count("1")  #bin(5)="0b101" <-str  #int("0b101",2)=5
            return a
#bin/int/hex
#http://www.cnblogs.com/pylemon/archive/2011/06/29/2093089.html

#Method 1+
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n>=2**32-1): 
            return 32
        else:
            num=0
            while n/2>0: #or n/2!=0
                if n%2==1:
                    num+=1
                n=int(n/2)
            if n==1:
                num+=1
            return num


#Method 1
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n>=2**32-1): 
            return 32
        else:
            arr=[]
            while n/2>0: #or n/2!=0
                if n%2==0:
                    arr.append(0)
                    n=int(n/2)
                elif n%2==1:
                    arr.append(1)
                    n=int(n/2)
            if n==1:
                arr.append(1)
            elif n==0:
                arr.append(0)
            num=arr.count(1)
            return num
           