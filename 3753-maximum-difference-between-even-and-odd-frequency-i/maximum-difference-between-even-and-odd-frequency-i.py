class Solution:
    def maxDifference(self, s: str) -> int:
        odd = 0
        even = len(s)
        count = Counter(s)

        for key, val in count.items():
            if val % 2 == 0:
                even = min(even, val)
            else:
                odd = max(odd, val)

        
        return odd - even