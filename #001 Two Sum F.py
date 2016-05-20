class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            n=target-nums[i]
            if n in nums and nums.index(n)!=i :
                return [i,nums.index(n)]

#时间换空间，最快，O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict={}
        for (i,value) in enumerate(nums):
            if nums_dict.has_key(target-value):
                return [nums_dict[target-value],i]
            else:
                nums_dict[value]=i

                
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers = sorted(num)  
  
        length = len(num)  
        left = 0  
        right = length - 1  
  
        index = []  
  
        while left < right:   
            sums = numbers[left] + numbers[right]  
  
            if sums == target:  
                for i in range(length):  
                    if num[i] == numbers[left]:  
                        index.append(i + 1)  
                    elif num[i] == numbers[right]:  
                        index.append(i + 1)  
                      
                    if len(index) == 2:  
                        break  
  
                break  
            elif sums > target:  
                right -= 1  
            else:  
                left += 1  
  
        result = tuple(index)  
  
        return result 