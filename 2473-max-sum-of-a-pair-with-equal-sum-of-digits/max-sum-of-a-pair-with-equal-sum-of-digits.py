class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)

        def total(num):
            res = 0

            while num:
                res += num % 10
                num = num // 10
            return res
        
        ans = -1
        for n in nums:
            sum = total(n)
            if sum in hashmap:
                ans = max(ans, n + hashmap[sum])
                hashmap[sum] = max(n, hashmap[sum])
            else:
                hashmap[sum] = n
        return ans


        