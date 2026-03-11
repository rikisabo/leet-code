class Solution(object):
    def minOperations(self, s):
        count1 = 0  # מול 010101...
        count2 = 0  # מול 101010...

        for i, ch in enumerate(s):
            expected1 = '0' if i % 2 == 0 else '1'
            expected2 = '1' if i % 2 == 0 else '0'

            if ch != expected1:
                count1 += 1
            if ch != expected2:
                count2 += 1

        return min(count1, count2)