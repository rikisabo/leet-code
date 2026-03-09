class Solution(object):
    def findDifferentBinaryString(self, nums):
        n = len(nums[0])
        arr = [False] * (2 ** n)

        for num in nums:
            cur = int(num, 2)
            arr[cur] = True

        for i in range(len(arr)):
            if not arr[i]:
                return bin(i)[2:].zfill(n)

        return ""
        
        
        