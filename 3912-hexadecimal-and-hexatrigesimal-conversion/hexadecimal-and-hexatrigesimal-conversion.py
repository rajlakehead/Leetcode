class Solution:
    def concatHex36(self, n: int) -> str:
        digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = ""
        n1 = n ** 2
        n2 = n ** 3
        res1 = ""
        res2 = ""

        while n1:
            num = n1 % 16
            res1 = digit_map[num] + res1
            n1 = n1 // 16
        
        while n2:
            num = n2 % 36
            res2 = digit_map[num] + res2
            n2 = n2 // 36

        return res1 + res2

        


        