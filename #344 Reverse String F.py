#344 Reverse String F

#Method1
class Solution(object):
    def reverseString(self, s):
        return s[::-1]

'''
[::] usage:
s[::-1] s逆序每一个取一个（即连续取）
s[::1] s顺序每一个取一个 (同s[::])
s[::2] s顺序每两个取一个（即隔一个取一个） “hello” -> "hlo"
s[::-2] 同上，逆序 “hello”->"olh"
'''

#Method2
class Solution(object):
    def reverseString(self, s):
        return "".join(reversed(s))

'''
reversed() 逆序
str.join() str接str
'''