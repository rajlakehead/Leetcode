class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictOfDigits = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        res = []
        combination = []
        def backtrack(i):
            if i >= len(digits):
                if len(combination[:]) == len(digits):
                    s = "".join(combination[:])
                    if s:
                        res.append(s)
                return
            
            for j in range(i, len(digits)):
                for idx in range(len(dictOfDigits[digits[j]])):
                    combination.append(dictOfDigits[digits[j]][idx])
                    backtrack(j + 1)
                    combination.pop()
        
        backtrack(0)
        return res

        