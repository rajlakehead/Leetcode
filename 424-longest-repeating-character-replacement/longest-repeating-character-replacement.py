class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        resLen, maxFeq = 0, 0
        counter = defaultdict(int)
        maxFeqChar = ""
        left = 0

        for right in range(len(s)):
            counter[s[right]] += 1
            if counter[s[right]] > maxFeq:
                maxFeq = counter[s[right]]
                maxFeqChqe = s[right]

            while (right - left + 1) - maxFeq > k:
                counter[s[left]] -= 1
                if s[left] == maxFeqChar:
                    maxFeq -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            
            resLen = max(resLen, (right - left + 1))

        return resLen


        