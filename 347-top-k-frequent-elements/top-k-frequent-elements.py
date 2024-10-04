class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)  # Get the frequency of each number
        hashmap = defaultdict(list)
        ans = []
        
        # Bucket sort: Group numbers by their frequency
        for num, freq in count.items():
            hashmap[freq].append(num)
        
        # Iterate from the largest frequency to the smallest
        for i in range(len(nums), 0, -1):
            if i in hashmap:  # Check if there are any numbers with this frequency
                for num in hashmap[i]:
                    ans.append(num)
                    if len(ans) == k:
                        return ans
        
        return ans