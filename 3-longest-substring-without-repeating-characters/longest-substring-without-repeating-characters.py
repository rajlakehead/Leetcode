class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        left, res = 0, 0

        for right in range(len(s)):
            counter[s[right]] += 1

            while len(counter) != (right - left + 1):
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            
            res = max(res, right - left + 1)

        return res