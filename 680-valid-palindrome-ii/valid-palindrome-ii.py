class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                new = s[left + 1: right + 1]
                new2 = s[left: right]
                if new == new[::-1] or new2 == new2[::-1]:
                    return True
                else:
                    return False
        return True