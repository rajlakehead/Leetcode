class Solution:
    def maxDiff(self, num: int) -> int:
        a = str(num)
        b = a

        pos = 0
        while pos < len(a) and a[pos] == "9":
            pos += 1

        if pos < len(a):
            a = a.replace(a[pos], "9")

        pos = 0
        while pos < len(b) and (b[pos] == "1" or b[pos] == "0"):
            pos += 1

        if pos < len(b):
            if pos != 0:
                b = b.replace(b[pos], "0")
            else:
                b = b.replace(b[pos], "1")

        return int(a) - int(b)