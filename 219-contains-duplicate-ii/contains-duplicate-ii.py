class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = defaultdict(int)

        for i, n in enumerate(nums):
            if n in hashmap:
                if abs(hashmap[n] - i) <= k:
                    return True
                hashmap[n] = i
            else:
                hashmap[n] = i
        return False

            