class Solution:
    def kthCharacter(self, k: int) -> str:
        lst = list("a")

        while len(lst) < k:
            temp = []

            for ch in lst:
                next = chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
                temp.append(next)
            lst.extend(temp)
        return lst[k - 1]
