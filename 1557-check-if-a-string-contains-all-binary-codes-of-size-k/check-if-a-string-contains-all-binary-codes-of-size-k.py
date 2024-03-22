class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hashset = set()

        for i in range(len(s) - k + 1):
            if s[i: i + k] not in hashset:
                hashset.add(s[i: i + k])
            
            if len(hashset) == 2 ** k:
                return True
        return False
        