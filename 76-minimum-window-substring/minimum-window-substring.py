class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        left = 0
        count = Counter(t)
        resLen = len(s) + 1
        need = len(count)

        for right in range(len(s)):
            count[s[right]] -= 1
            if count[s[right]] == 0:
                del count[s[right]]
                need -= 1
            
            while need == 0:
                count[s[left]] += 1
                if count[s[left]] == 1:
                    need += 1
                if resLen > (right - left + 1):
                    res = s[left : right + 1]
                    resLen = (right - left + 1)
                left += 1

        return res
        