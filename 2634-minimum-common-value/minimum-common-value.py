class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for n in nums1:
            idx1 = bisect.bisect_left(nums2, n)
            idx2 = bisect.bisect_right(nums2, n)

            if idx1 != idx2:
                return n
        return -1    

        