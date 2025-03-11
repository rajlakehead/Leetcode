class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        h = []
        res = ""
        
        for c in set(s):
            heapq.heappush(h, (-count[c], c))
        
        print(h)
        
        while len(h) >= 2:
            feq1, char1 = heapq.heappop(h)
            feq2, char2 = heapq.heappop(h)

            res += char1
            res += char2

            feq1 += 1
            feq2 += 1

            if feq1 != 0:
                heapq.heappush(h, (feq1, char1))
            
            if feq2 != 0:
                heapq.heappush(h, (feq2, char2))
        
        if h and h[0][0] < -1:
            return ""
        elif h:
            res += h[0][1]
            return res
        else:
            return res

