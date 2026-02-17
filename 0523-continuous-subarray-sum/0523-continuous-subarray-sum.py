class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {0: -1}
        s = 0

        for i, x in enumerate(nums):
            s += x
            r = s % k
    
            if r in seen:
                if i - seen[r] >= 2:
                    return True
            else:
                seen[r] = i

        return False
            

        

            

            
        
        