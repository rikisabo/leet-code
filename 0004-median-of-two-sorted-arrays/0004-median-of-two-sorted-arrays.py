class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # מוודאים ש-nums1 הוא תמיד המערך הקצר יותר כדי לייעל את החיפוש
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            # חיתוך במערך הראשון
            partition1 = (low + high) // 2
            # חיתוך משלים במערך השני
            partition2 = (m + n + 1) // 2 - partition1
            
            # הגדרת הערכים סביב נקודות החיתוך (עם טיפול בקצוות)
            maxLeft1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            minRight1 = nums1[partition1] if partition1 < m else float('inf')
            
            maxLeft2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            minRight2 = nums2[partition2] if partition2 < n else float('inf')
            
            # בדיקה האם מצאנו את נקודת האיזון הנכונה
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # אם סך האיברים אי-זוגי, החציון הוא הערך המקסימלי בצד שמאל
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                # אם זוגי, ממוצע של המקסימום משמאל והמינימום מימין
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            
            elif maxLeft1 > minRight2:
                # אנחנו יותר מדי ימינה במערך הראשון, נזוז שמאלה
                high = partition1 - 1
            else:
                # אנחנו יותר מדי שמאלה במערך הראשון, נזוז ימינה
                low = partition1 + 1
                
        return 0.0