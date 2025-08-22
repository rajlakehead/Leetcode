class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substrings = set()
        left = 0

        for right in range(len(s)):

            if right - left + 1 == k:
                substrings.add(s[left: right + 1])
                left += 1
        
        return len(substrings) == 2 ** k