from collections import defaultdict
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = defaultdict(int)
        res = 0
        has_odd_center = False

        for word in words:
            count[word] += 1

        for word in list(count.keys()):
            rev = word[::-1]
            if word != rev:
                # Match word and its reverse
                if rev in count:
                    pair_count = min(count[word], count[rev])
                    res += pair_count * 4
                    count[word] -= pair_count
                    count[rev] -= pair_count
            else:
                # Palindromic word like "gg", "cc"
                pairs = count[word] // 2
                res += pairs * 4
                count[word] -= pairs * 2
                if count[word] == 1:
                    has_odd_center = True

        if has_odd_center:
            res += 2  # one central palindromic word

        return res
