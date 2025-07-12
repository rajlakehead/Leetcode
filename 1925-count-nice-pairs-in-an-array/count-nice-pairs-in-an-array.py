class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        def reverse(n):
            rev = 0

            while n:
                digit = n % 10
                rev = rev * 10 + digit
                n //= 10
            return rev

        hashmap = defaultdict(int)
        res = 0

        for n in nums:
            diff = n - reverse(n)
            res = (res + hashmap[diff]) % MOD
            hashmap[diff] += 1
        return res
        



