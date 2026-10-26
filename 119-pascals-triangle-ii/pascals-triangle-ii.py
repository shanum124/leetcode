class Solution:
    def getRow(self, i: int) -> list[int]:
        row = [1]
        value = 1
        for j in range(1, i + 1):
            value = value * (i - j + 1) // j
            row.append(value)
        return row


