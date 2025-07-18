class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        res = 0
        length = 0

        for n in nums:
            if n % 2 == 0:
                length += 1

        res = max(res, length)
        length = 0

        for n in nums:
            if n % 2 != 0:
                length += 1

        res = max(res, length)
        length = 1
        flag = True
        if nums[0] % 2 != 0:
            flag = False

        for i in range(1, len(nums)):
            if flag:
                if nums[i] % 2 != 0:
                    length += 1
                    flag = False
            else:
                if nums[i] % 2 == 0:
                    length += 1
                    flag = True
        res = max(res, length)
        return res




