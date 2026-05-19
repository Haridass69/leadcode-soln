class Solution:
    def coinChange(self, coins, amount):

        # Initialize DP array
        dp = [float('inf')] * (amount + 1)

        # Base case
        dp[0] = 0

        # Fill DP array
        for i in range(1, amount + 1):

            for coin in coins:

                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If amount cannot be formed
        if dp[amount] == float('inf'):
            return -1

        return dp[amount]