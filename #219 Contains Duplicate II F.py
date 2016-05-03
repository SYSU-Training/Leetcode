#219. Contains Duplicate II 
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
