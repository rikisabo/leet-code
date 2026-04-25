#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        // 1. יצירת ווקטור של זוגות: {ערך, אינדקס מקורי}
        std::vector<std::pair<int, int>> indexedNums;
        for (int i = 0; i < nums.size(); ++i) {
            indexedNums.push_back({nums[i], i});
        }

        // 2. מיון לפי הערכים (האיבר הראשון בזוג)
        std::sort(indexedNums.begin(), indexedNums.end());

        // 3. שימוש בשני מצביעים על הווקטור הממוין
        int left = 0;
        int right = indexedNums.size() - 1;

        while (left < right) {
            int sum = indexedNums[left].first + indexedNums[right].first;

            if (sum == target) {
                // החזרת האינדקסים המקוריים שנשמרו בתוך הזוג
                return {indexedNums[left].second, indexedNums[right].second};
            }
            else if (sum < target) {
                left++;
            }
            else {
                right--;
            }
        }

        return {}; // במקרה שלא נמצא פתרון
    }
};