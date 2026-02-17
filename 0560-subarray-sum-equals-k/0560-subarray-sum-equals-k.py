class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h={}
        prev = 0
        res = 0
        for num in nums:
            cur = num +prev
            if cur == k:
                res+=1
            res+= h.get(cur-k,0)
            if h.get(cur):
                h[cur]+=1
            else:
                h[cur]=1
            prev=cur
        return res
            

        
        