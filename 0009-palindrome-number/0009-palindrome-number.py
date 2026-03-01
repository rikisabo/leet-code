class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x>=0 and x<10:
            return True
        digits= len(str(abs(x)))
       


        s=str(abs(x))
        half=digits//2

        stack=[]
        for ch in s[:half]:
            stack.append(ch)
        
        if digits%2==1:
            i=digits//2+1
        else:
            i=digits//2
        for digit in s[i:]:
            if digit!=stack.pop():
                return False
        return True

            