from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # שלב 1: טרנספוזיציה (החלפת מטריצה [i][j] ב-[j][i])
        # אנו עוברים רק על המשולש העליון של המטריצה כדי לא להחליף פעמיים
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # שלב 2: שיקוף כל שורה (הפיכת סדר האיברים)
        for i in range(n):
            matrix[i].reverse()