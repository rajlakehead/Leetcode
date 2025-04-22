class Solution:
    def smallestPalindrome(self, s: str) -> str:
        feq = Counter(s)
        left = ""
        mid = ""

        for ch in sorted(feq.keys()):
            count = feq[ch]

            if count % 2 != 0:
                mid = ch
                count -= 1
            left += ch * (count // 2)
        
        right = left[::-1]
        return left + mid + right

