# https://www.youtube.com/watch?v=_GF-0T-YjW8
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9+7
        cnt = defaultdict(int)
        for wd in words:
            for i,ch in enumerate(wd):
                cnt[(i,ch)]+=1

        memo = {}
        def dfs(i,k): # i is index of target and k in index of jth word (word[j][k])
            if i==len(target):
                return 1
            if k==len(words[0]):
                return 0
            if (i,k) in memo:
                return memo[(i,k)]
            c=target[i]
            memo[(i,k)]=dfs(i,k+1) # skipping kth position
            memo[(i,k)]+= cnt[(k,c)]*dfs(i+1,k+1)
            return memo[(i,k)] % mod
        return dfs(0,0)