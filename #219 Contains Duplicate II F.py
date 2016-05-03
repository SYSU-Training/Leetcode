#219. Contains Duplicate II 
'''
Method 1
http://www.cnblogs.com/sxbjdl/p/5281389.html
'''
def fun(num,k):
    d={}  #name->integer  value->position from 0
    for i,v in enumerate(num):  #enumerate()->tuple
        if v in d and i-d[v]<=k: 
            return True
        d[v]=i  #old one covers the new one if equal value and >k
    return False

'''
Method 2
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)==len(list(set(nums))):
            return False
        for i in range(len(nums)):
            for j in range(i+1,min(k+1+i,len(nums))):
                if nums[i]==nums[j]:
                    return True
        return False
