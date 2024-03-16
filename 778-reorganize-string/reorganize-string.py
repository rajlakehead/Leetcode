class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = []
        for c in count:
            maxheap.append((-count[c], c))
        res = ""
        heapq.heapify(maxheap)
        prev = None

        while maxheap or prev:

            if prev and not maxheap:
                return ""

            if maxheap:
                cnt, char = heapq.heappop(maxheap)
                res += char
                cnt += 1

            if prev:
                heapq.heappush(maxheap, (prev[0], prev[1]))
                prev = None

            if cnt:
                prev = [cnt, char]

        return res

        