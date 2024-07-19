class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        minIndex = 0
        targetIndex = 0

        def condition(idx):
            if nums[0] <= nums[idx]:
                return False
            return True
        
        def binarySearch(left, right, search):

            while left < right:
                mid = left + (right - left) // 2

                if search:
                    if nums[mid] >= target:
                        right = mid
                    else:
                        left = mid + 1
                else:
                    if condition(mid):
                        right = mid
                    else:
                        left = mid + 1
            
            return left
        
        left = binarySearch(left, right, False)
        print(left)

        if nums[0] < nums[left]:
            minIndex = 0
        else:
            minIndex = left
        
        print(minIndex)
        if target >= nums[minIndex] and target <= nums[len(nums) - 1]:
            targetIndex = binarySearch(minIndex, len(nums) - 1, True)
        else:
            targetIndex = binarySearch(0, minIndex - 1, True)
        
        print(targetIndex)
        if nums[targetIndex] == target:
            return targetIndex
        return -1
