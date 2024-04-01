class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        need = len(count)
        left = 0
        res = []

        for right in range(len(s)):
            count[s[right]] -= 1
            if count[s[right]] == 0:
                need -= 1

            if (right - left + 1) == len(p):
                if need == 0:
                    res.append(left)
                count[s[left]] += 1
                if count[s[left]] == 1:
                    need += 1
                left += 1
                
        return res




        