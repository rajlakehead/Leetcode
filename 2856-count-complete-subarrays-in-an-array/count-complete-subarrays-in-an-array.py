class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        n, k = len(nums), len(set(nums))
        res = i = 0
        count = Counter()
        for j in range(n):
            count[nums[j]] += 1
            while len(count) == k:
                count[nums[i]] -= 1
                if count[nums[i]] == 0:
                    del count[nums[i]]
                i += 1
            res += i
        return res

         # Step 1: Calculate the total number of distinct elements in the entire array
        total_distinct = len(set(nums))  # This gives us the number of distinct elements in the array
        n = len(nums)
        left = 0
        count = 0
        freq_map = {}

        # Step 2: Use the sliding window technique
        for right in range(n):
            # Add the current element to the window
            if nums[right] in freq_map:
                freq_map[nums[right]] += 1
            else:
                freq_map[nums[right]] = 1
            
            # Shrink the window if we have more distinct elements than needed
            while len(freq_map) == total_distinct:
                # Count all subarrays starting from 'left' and ending at 'right'
                count += n - right  # All subarrays [left, right], [left, right + 1], ..., [left, n-1] are valid

                # Shrink the window from the left
                freq_map[nums[left]] -= 1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]  # Remove the element if its count becomes zero
                left += 1

        return count