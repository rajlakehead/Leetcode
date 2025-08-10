class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        c = Counter(str(n))

        for i in range(33):
            if c == Counter(str(2 ** i)):
                return True
        return False