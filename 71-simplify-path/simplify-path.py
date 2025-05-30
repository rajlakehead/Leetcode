class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split("/")
        res = []
        
        for curr in lst:
            if curr == "" or curr == ".":
                continue

            elif curr == "..":
                if res:
                    res.pop()
            else:
                res.append(curr)

        return "/" + "/".join(res)
            
            