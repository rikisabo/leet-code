class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map_ = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(s)-1):
            cur = map_[s[i]]
            nxt = map_[s[i+1]]
            if nxt > cur:
                total = total-cur
            else:
                total= total+cur
        total=total+map_[s[len(s)-1]]
        return total


        