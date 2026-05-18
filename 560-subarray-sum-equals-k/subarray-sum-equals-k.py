class Solution:

    def subarraySum(self, nums, k):

        count = 0
        prefix_sum = 0

        # Dictionary to store prefix sum frequency
        prefix_count = {0: 1}

        for num in nums:

            prefix_sum += num

            # Check if there exists a prefix sum
            # such that current_sum - old_sum = k
            if (prefix_sum - k) in prefix_count:
                count += prefix_count[prefix_sum - k]

            # Store current prefix sum
            if prefix_sum in prefix_count:
                prefix_count[prefix_sum] += 1
            else:
                prefix_count[prefix_sum] = 1

        return count