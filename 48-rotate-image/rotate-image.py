class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        se = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if (i,j) in se or (j,i) in se:
                    continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                se.add((i,j))
                se.add((j,i))
        print(matrix)
        for i in matrix:
            i.reverse()
        # return matrix