class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        left = 0
        length = len(count)



        for right in range(len(s2)):
            count[s2[right]] -= 1

            if count[s2[right]] == 0:
                length -= 1
            
            if (right - left + 1) == len(s1):
                if length == 0:
                    return True
                
                count[s2[left]] += 1
                if count[s2[left]] == 1:
                    length += 1

                left += 1
        return False