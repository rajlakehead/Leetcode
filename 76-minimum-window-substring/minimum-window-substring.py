class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        need = len(count)
        res = len(s) + 1
        ans = ""
        left = 0

        for right in range(len(s)):
            count[s[right]] -= 1
            if count[s[right]] == 0:
                need -= 1
                del count[s[right]]
            
            while need == 0:
                if (right - left + 1) < res:
                    ans = s[left: right + 1]
                    res = (right - left + 1)
                count[s[left]] += 1
                if count[s[left]] == 1:
                    need += 1
                left += 1
        return ans
