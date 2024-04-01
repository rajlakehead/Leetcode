class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = float('-inf')
        left = 0
        currmax = 0

        for right in range(len(s)):
            count[s[right]] += 1
            currmax = max(currmax, count[s[right]])

            while (right - left + 1) - currmax > k:
                count[s[left]] -= 1
                currmax = max(count.values())
                left += 1
            res = max(res, right - left + 1)
        return res

        