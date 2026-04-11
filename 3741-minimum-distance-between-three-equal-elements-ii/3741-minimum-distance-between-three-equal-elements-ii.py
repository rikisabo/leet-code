class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return -1
        counts={}
        indices={}
        min_dist=float('inf')
        found=False
        
        for idx, val in enumerate(nums):
            if val in counts:
                counts[val]+=1
            else:
                counts[val]=1
            if val not in indices:
                indices[val]=[]
            indices[val].append(idx)
            if counts[val]>=3:
                found=True
                if len(indices[val])>=3:
                    cur_dist=abs(indices[val][-1]-indices[val][-3])
                    if cur_dist*2 < min_dist:
                        min_dist= cur_dist*2
        return min_dist if found else -1
        