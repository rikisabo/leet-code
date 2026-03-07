class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        ans = strs[0]
        for i in range(len(ans)):
            for st in strs[1:]:
                if i>=len(st) or st[i]!=ans[i] :
                    return ans[:i]
        return ans




        