#168
class Solution(object):
    def convertToTitle(self, num):
        """
        :type s: int
        :rtype: str
        """
        result = ''
        while num:
            result = chr(ord('A') + (num-1)%26) + result
            num = (num -1)/26
        return result