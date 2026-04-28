class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack; // עדיף char עבור תווים

        for (char c : s) {
            // אם זה סוגר פותח, פשוט דוחפים למחסנית
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } 
            // אם זה סוגר סוגר
            else {
                // בדיקה אם יש בכלל סוגר פותח שמתאים לו
                if (stack.empty()) return false;
                
                char top = stack.top();
                if ((c == ')' && top == '(') || 
                    (c == '}' && top == '{') || 
                    (c == ']' && top == '[')) {
                    stack.pop(); // התאמה נמצאה, מסירים וממשיכים
                } else {
                    return false; // סוגר לא מתאים
                }
            }
        }

        // בסוף, המחסנית חייבת להיות ריקה (כל סוגר שנפתח גם נסגר)
        return stack.empty();
    }
};