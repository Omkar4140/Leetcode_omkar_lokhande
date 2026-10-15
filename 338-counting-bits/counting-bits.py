class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0]
        for i in range(1,n+1):
            result.append(result[i//2]+ i % 2)
        return result
        