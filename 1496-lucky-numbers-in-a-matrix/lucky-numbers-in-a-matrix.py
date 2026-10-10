class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        col = len(matrix[0])

        min_rows = []
        for i in range(row):
            row_min = min(matrix[i])
            min_rows.append(row_min)

        max_cols = []
        for i in range(col):
            col_max = matrix[0][i]
            for j in range(row):
                if matrix[j][i] > col_max:
                    col_max = matrix[j][i]
            max_cols.append(col_max)

        lucky = []
        for i in range(row):
            for j in range(col):
                curr = matrix[i][j]
                if curr == min_rows[i] and curr == max_cols[j]:
                    lucky.append(curr)
        return lucky


        