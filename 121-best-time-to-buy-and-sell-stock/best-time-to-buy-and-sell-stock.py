class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit =0

        for i in prices:
            if i < min_price:
                min_price = i
            else:
                max_profit = max(max_profit, i - min_price)
        return max_profit
        # best=0
        # n= len(prices)

        # for i in range(n):
        #     for j in range(i +1, n):
        #         diff = prices[j]- prices[i]
        #         if diff > best:
        #             best = diff
        # return best

        