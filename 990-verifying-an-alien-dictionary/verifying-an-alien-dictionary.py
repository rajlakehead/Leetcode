class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = defaultdict(int)

        for i, char in enumerate(order):
            hashmap[char] = i
        
        for idx in range(len(words) - 1):
            w1, w2 = words[idx], words[idx + 1]

            for j in range(len(w1)):

                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if hashmap[w1[j]] > hashmap[w2[j]]:
                        return False
                    break
        return True

        
