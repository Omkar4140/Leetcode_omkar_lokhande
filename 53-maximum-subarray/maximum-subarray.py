class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_max=0
        max_so_far=nums[0]
        for i in nums:
            curr_max=max(i,i+curr_max)       
            max_so_far = max(max_so_far,curr_max)
        return max_so_far 