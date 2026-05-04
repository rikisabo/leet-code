class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
    # אם האורכים שונים, זה בלתי אפשרי
        if len(s) != len(goal):
            return False
    
    # בדיקה האם goal נמצא בתוך s + s
        return goal in (s + s)
        