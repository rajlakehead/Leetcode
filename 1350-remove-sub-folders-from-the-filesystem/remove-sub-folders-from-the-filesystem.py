class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        hashset = set()
        folder.sort()
        res = []

        for f in folder:
            lst = f[1:].split("/")
            new = "/"
            for i in range(len(lst)):
                new += lst[i]
                if new in hashset:
                    break
                new += "/"
            else:
                hashset.add("/" + "/".join(lst))
                res.append(f)
                    
        return res

        