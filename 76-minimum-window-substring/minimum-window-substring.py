class Solution:

    def minWindow(self, s, t):

        if not s or not t:
            return ""

        # Count characters in t
        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        required = len(need)
        formed = 0

        window = {}

        left = 0
        min_len = float("inf")
        result = ""

        for right in range(len(s)):

            char = s[right]

            # Add current character to window
            window[char] = window.get(char, 0) + 1

            # Check if character count matches
            if char in need and window[char] == need[char]:
                formed += 1

            # Try shrinking window
            while left <= right and formed == required:

                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                left_char = s[left]

                # Remove left character
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return result