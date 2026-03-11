class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        mismatch1=0
        mismatch2=0
        for i,ch in enumerate(s):
            ch1= '0' if i%2==0 else '1'
            ch2= '1' if i%2==0 else '0'
            if ch!=ch1:
                mismatch1+=1

            if ch!=ch2:
                print(ch2,ch)
                mismatch2+=1
        return min(mismatch1,mismatch2)


        

        