class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        map = {'a':a,'b':b,'c':c}
        heap = []
        for key,val in map.items():
            if val!=0:
                heap.append((-val,key))
        heapify(heap)
        ans = ''
        while heap:
            count,char = heappop(heap)
    
            if len(ans)>1 and ans[-1]==ans[-2]==char:
                if heap:
                    count2,char2 = heappop(heap)
                    heappush(heap,(count,char))
                    ans+=char2
                    if count2!=-1:
                        heappush(heap,(count2+1,char2))
            else:
                ans+=char
                if count!=-1:
                    heappush(heap,(count+1,char))
        return(ans)
                
            