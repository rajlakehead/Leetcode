class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = set()

        l, r = 0, 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                l += 1
            elif nums2[r] < nums1[l]:
                r += 1
            else:
                res.add(nums1[l])
                r += 1
                l += 1
        
        return list(res)


        