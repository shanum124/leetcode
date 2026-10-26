class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # res = [1]
        row = [comb(rowIndex, j) for j in range(rowIndex + 1)]
        return row


