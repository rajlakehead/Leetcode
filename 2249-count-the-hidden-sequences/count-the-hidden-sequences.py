class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        cur = 0
        min_offset = 0
        max_offset = 0

        for diff in differences:
            cur += diff
            min_offset = min(min_offset, cur)
            max_offset = max(max_offset, cur)

        # possible start value range
        start_min = lower - min_offset
        start_max = upper - max_offset

        return max(0, start_max - start_min + 1)