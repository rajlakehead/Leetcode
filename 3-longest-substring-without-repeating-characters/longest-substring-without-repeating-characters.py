class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(int)
        left = 0
        res = 0

        for right in range(len(s)):
            hashmap[s[right]] += 1

            if (right - left + 1) > len(hashmap):
                hashmap[s[left]] -= 1

                if hashmap[s[left]] == 0:
                    del hashmap[s[left]]
                
                left += 1
            
            res = max(res, (right - left + 1))

        return res