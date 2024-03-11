class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        ans = []
        
        subs = defaultdict(list)
        
        for idx,s in enumerate(arr):
            for i in range(len(s)):
                for j in range(i+1, len(s)+1):
                    subs[idx].append(s[i:j])
            subs[idx].sort(key=lambda x:(len(x), x))
        
        for s1,sub1 in subs.items():
            cur_ans = ""
            for substring1 in sub1:
                flag = 1
                for s2,sub2 in subs.items():
                    if s1!=s2 and (substring1 in sub2):
                        flag = 0
                        break
                if flag:
                    cur_ans = substring1
                    break
            ans.append(cur_ans)
        
        return ans