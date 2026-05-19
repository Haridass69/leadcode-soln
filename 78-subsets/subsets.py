class Solution:
    def subsets(self, nums):

        result = []

        def backtrack(index, current):

            # Add current subset
            result.append(current[:])

            for i in range(index, len(nums)):

                # Choose element
                current.append(nums[i])

                # Recurse
                backtrack(i + 1, current)

                # Backtrack
                current.pop()

        backtrack(0, [])

        return result