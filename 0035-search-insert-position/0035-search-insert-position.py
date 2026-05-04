import bisect

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # הפונקציה bisect_left מוצאת את האינדקס שבו target צריך להיכנס 
        # כדי לשמור על המערך ממוין. אם הוא כבר קיים, היא תחזיר את האינדקס שלו.
        return bisect.bisect_left(nums, target)