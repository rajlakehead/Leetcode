class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        vowels = 0
        left = 0
        for right in range(len(s)):
            if s[right] in "aeiou":
                vowels += 1
            if (right - left + 1) >= k:
                res = max(res, vowels)
                if s[left] in "aeiou":
                    vowels -= 1
                left += 1
        return res