class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hashmap = defaultdict(int)

        if len(hand) % groupSize != 0:
            return False


        for n in hand:
            hashmap[n] += 1
        
        print(hashmap)

        minheap = list(hashmap.keys())
        heapq.heapify(minheap)


        while minheap:
            start = minheap[0]

            for i in range(start, start + groupSize):
                if i not in hashmap:
                    return False
                hashmap[i] -= 1
                if hashmap[i] == 0:
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)


        return True
            

