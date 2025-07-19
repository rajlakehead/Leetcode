class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]

        for i in range(1, len(folder)):
            parent = res[-1]
            parent += "/"

            if not folder[i].startswith(parent):
                res.append(folder[i])
        return res


        