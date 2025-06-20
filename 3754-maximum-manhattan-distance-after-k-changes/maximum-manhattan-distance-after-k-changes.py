class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        ans = 0
        dirs_sum = 0 
        for c in s:
            freq[c] += 1
            dirs_sum += 1 # dirs_sum = sum(freq.values())
            num_of_opposite_dirs = min(freq["N"], freq["S"]) + min(freq["W"], freq["E"])
            # Current manhattan distance can be calculated by subtracting the
            # 2 * num_of_opposite_dirs from the sum of all directions.
            # Such direction will cancel the effect of itself
            # and opposing direction, thus twice the reduction.
            man_dis = dirs_sum - (2 * num_of_opposite_dirs) 
            # Simulate changing upto min(k, num_of_opposite_dirs) directions.
            # Such move will undo the effect done by the opposing direction.
            man_dis += (2 * min(k, num_of_opposite_dirs))
            ans = max(ans, man_dis)
        return ans