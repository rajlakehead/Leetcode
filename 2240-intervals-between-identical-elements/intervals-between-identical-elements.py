class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        hashmap = {}
        ans = [0] * len(arr)

        for i, n in enumerate(arr):
            if n in hashmap:
                hashmap[n].append(i)
            else:
                hashmap[n] = [i]
        
        for index in hashmap.values():
            prefixSum = 0
            suffixSum = sum(index)
            pre = 0
            suff = len(index)

            for idx in range(len(index)):
                pre += 1
                prefixSum += index[idx]
                suff -= 1
                suffixSum -= index[idx]

                ans[index[idx]] = (pre * index[idx] - prefixSum) + (suffixSum - (suff * index[idx]))
        
        return ans


