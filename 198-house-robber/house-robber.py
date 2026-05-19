class Solution:
    def rob(self, nums):

        # Base cases
        if len(nums) == 1:
            return nums[0]

        prev2 = 0   # dp[i-2]
        prev1 = 0   # dp[i-1]

        for money in nums:
            current = max(prev1, prev2 + money)

            prev2 = prev1
            prev1 = current

        return prev1