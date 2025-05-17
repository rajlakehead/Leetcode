class Solution:
    def getWordsInLongestSubsequence(self, words, groups):
        def hamming(s1, s2):
            if len(s1) != len(s2):
                return False
            diff_count = sum(c1 != c2 for c1, c2 in zip(s1, s2))
            return diff_count == 1

        LIS = [1 for _ in range(len(words))]
        prev = [-1] * len(words)


        for i in range(len(words) - 2, -1, -1):
            for j in range(i + 1, len(words)):
                if groups[i] != groups[j] and hamming(words[i], words[j]):
                    if LIS[i] < 1 + LIS[j]:
                        LIS[i] = 1 + LIS[j]
                        prev[i] = j
        max_len = max(LIS)
        max_start_index = LIS.index(max_len)
        res = []

        while max_start_index != -1:
            res.append(words[max_start_index])
            max_start_index = prev[max_start_index]

        return res







        res = []

        @lru_cache(None)
        def dp(i, curr, prev):
            nonlocal res
            if i >= len(words):
                if len(curr) > len(res):
                    res = curr.copy()
                return

            # Option 1: skip words[i]
            dp(i + 1, curr, prev)

            # Option 2: include words[i] if valid
            if prev == -1 or (groups[i] != groups[prev] and hamming(words[i], words[prev])):
                curr.append(words[i])
                dp(i + 1, curr, i)
                curr.pop()  # backtrack

        dp(0, [], -1)
        return res
