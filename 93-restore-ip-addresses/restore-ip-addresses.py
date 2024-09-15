class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        parts = []

        def backtrack(i):
            if i == len(s) and len(parts) == 4:
                res.append(".".join(parts))
                return

            # Early stopping: if we already have 4 parts and haven't finished the string, it's invalid
            if len(parts) == 4:
                return

            for j in range(i, min(i + 3, len(s))):
                # Get the current part of the string
                address = s[i:j + 1]
                
                # Check if the part is a valid segment
                if int(address) <= 255 and (len(address) == 1 or address[0] != '0'):
                    parts.append(address)
                    backtrack(j + 1)
                    parts.pop()

        backtrack(0)
        return res
