class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        has = {
            "right": "down",
            "down": "left",
            "left": "up",
            "up": "right"
        }
        x = "right"
        res = []
        k = 0
        i = 0
        j = 0
        m = len(matrix)
        n = len(matrix[0])
        while k<m*n:
            if x=="right":
                if 0 <= i < m and 0 <= j < n and matrix[i][j] != "v":
                    res.append(matrix[i][j])
                    matrix[i][j] = "v"
                    j+=1
                    k+=1
                    print(res)
                else:
                     j -= 1
                     i += 1
                     x = has[x]
            elif x=="down":
                if 0 <= i < m and 0 <= j < n and matrix[i][j] != "v":
                    res.append(matrix[i][j])
                    matrix[i][j] = "v"
                    i+=1
                    k+=1
                else:
                    i -= 1
                    j -= 1
                    x = has[x]
            elif x=="left":
                if 0 <= i < m and 0 <= j < n and matrix[i][j] != "v":
                    res.append(matrix[i][j])
                    matrix[i][j] = "v"
                    j-=1
                    k+=1
                else:
                    j+=1
                    i-=1
                    x = has[x]
            elif x=="up":
                if 0 <= i < m and 0 <= j < n and matrix[i][j] != "v":
                    res.append(matrix[i][j])
                    matrix[i][j] = "v"
                    i-=1
                    k+=1
                else:
                    i += 1
                    j += 1
                    x = has[x]
        return res