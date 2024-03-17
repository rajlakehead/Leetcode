class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        d = Counter(word)
        self.memo = {}
        freq = sorted(list(d.values()))                         #sort frequencies
        return self.f(0,len(freq)-1, k, freq)

    def f(self, i, j, k, freq):
        #if the difference between max and min frequencies <= k, then all frequencies would be at most k distance apart.
        if abs(freq[i] - freq[j]) <= k:            
            return 0

        if (i,j) not in self.memo:
            a = b = float('inf')
            a = freq[i] + self.f(i+1, j,k, freq)                #either delete all characters of smaller frequency
            b = freq[j] - freq[i] - k + self.f(i,j-1,k,freq)    #or remove just enough characters of higher frequency as to make difference = k
                                                                #shift edges i or j accordingly
            self.memo[(i,j)] = min(a,b)                         #memoize the result for future.
        return self.memo[(i,j)]
    
        