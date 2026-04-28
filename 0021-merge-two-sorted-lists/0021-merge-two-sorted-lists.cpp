/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    ListNode dummy(0); // צומת זמני על המחסנית
    ListNode* tail = &dummy; // מצביע שעוזר לנו לרוץ ולבנות את הרשימה

    while (list1 != nullptr && list2 != nullptr) {
        if (list1->val < list2->val) {
            tail->next = list1; // מחברים את הצומת הקיים במקום ליצור חדש (יעיל יותר)
            list1 = list1->next;
        } else {
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }

    // חיבור השארית של הרשימה שלא הסתיימה
    tail->next = (list1 != nullptr) ? list1 : list2;

    return dummy.next; // מחזירים את הצומת שאחרי ה-dummy
}
};