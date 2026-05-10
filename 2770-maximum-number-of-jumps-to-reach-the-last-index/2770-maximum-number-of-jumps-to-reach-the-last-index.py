class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # מאתחלים במינוס 1 כדי לסמן מקומות שלא הגענו אליהם עדיין
        dp = [-1] * n
        dp[0] = 0  # אנחנו מתחילים באינדקס 0, אז שם יש 0 קפיצות
        
        for i in range(1, n):
            for j in range(i):
                # בדיקה 1: האם ניתן להגיע לאינדקס j בכלל?
                # בדיקה 2: האם ההפרש בין הערכים ב-nums עומד בתנאי ה-target?
                if dp[j] != -1 and abs(nums[i] - nums[j]) <= target:
                    # עדכון מספר הקפיצות המקסימלי לאינדקס i
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return dp[n-1]