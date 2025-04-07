class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        left = nums1[:m + 1]
        k = 0
        i, j = 0, 0
        
        while i < m and j < n:

            if left[i] <= nums2[j]:
                nums1[k] = left[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            
            k += 1
        
        while i < m:
            nums1[k] = left[i]
            i += 1
            k += 1
        while j < n:
            nums1[k] = nums2[j]
            k += 1
            j += 1
            

        