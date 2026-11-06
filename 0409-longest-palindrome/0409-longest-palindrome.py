class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic={}
        l=0
        odd=0
        for i in s:
            dic[i] = dic.get(i,0) + 1
        
        for k,v in dic.items():
            if dic[k] %2 == 0:
                l+=v
            else:
                l+=v-1
                if odd < v:
                    odd=v
        if odd>0:
            l+=1
        return l

        