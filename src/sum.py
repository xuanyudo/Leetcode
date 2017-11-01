class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = 0
        
        num = nums.pop(0)
        while (target-num) not in nums:
            first+=1
            num = nums.pop(0)
        
        second = nums.index(target-num)+first+1
        return [first,second]