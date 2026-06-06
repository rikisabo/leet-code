#include <vector>
using namespace std;

class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size(); // תיקון: שימוש ב-size() במקום length()
        int len2 = nums2.size();
        
        // בדיקת קצה חכמה שהוספת - אם אין סיכוי לחפיפה
        if (nums1[len1 - 1] < nums2[0] || nums2[len2 - 1] < nums1[0]) {
            return -1;
        }
        
        // תיקון: לקיחת הכתובת של האיבר הראשון באמצעות &
        int* p1 = &nums1[0];
        int* p2 = &nums2[0];
        
        // הגדרת פוינטרים לסוף המערכים כדי לדעת מתי לעצור
        int* end1 = &nums1[len1];
        int* end2 = &nums2[len2];
        
        // הלולאה רצה כל עוד שני הפוינטרים מצביעים על איברים חוקיים
        while (p1 < end1 && p2 < end2) {
            if (*p1 == *p2) {
                return *p1;
            }
            else if (*p1 < *p2) {
                p1++;
            }
            else {
                p2++;
            }
        }
        
        // אם הגענו לכאן, לא נמצא אף איבר משותף
        return -1;
    }
};