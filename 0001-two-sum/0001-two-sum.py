class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [(val, i)for i, val in enumerate(nums)]
        nums.sort(key=lambda x: x[0])
        
        left=0
        right=len(nums)-1

        while left<right:
            s= nums[right][0]+nums[left][0]
            if s==target:
                return nums[left][1], nums[right][1]
            if s<target:
                left+=1
            if s>target:
                right-=1
        return None