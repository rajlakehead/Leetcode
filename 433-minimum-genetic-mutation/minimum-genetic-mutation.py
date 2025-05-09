class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = [(0, startGene)]
        visited = set()

        while q:
               
            for _ in range(len(q)):
                steps, gene = q.pop(0)

                if gene == endGene:
                    return steps
            
                visited.add(gene)
                for i in range(8):
                    genelst = list(gene)
                    for char in "ACGT":
                        genelst[i] = char
                        currgene = "".join(genelst)
                        if currgene not in visited and currgene in bank:
                            q.append((steps + 1, currgene))
                            visited.add(currgene)

        return -1

