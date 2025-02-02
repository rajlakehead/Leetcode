class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashmap = defaultdict(int)

        for bill in bills:
            if bill == 5:
                hashmap[5] += 1
            elif bill == 10:
                if hashmap[5] == 0:
                    return False
                hashmap[5] -= 1
                hashmap[10] += 1
            else:
                if (hashmap[5] > 0 and hashmap[10] > 0):
                    hashmap[5] -= 1
                    hashmap[10] -= 1
                elif hashmap[5] >= 3:
                    hashmap[5] -= 3
                else:
                    return False

        return True
        