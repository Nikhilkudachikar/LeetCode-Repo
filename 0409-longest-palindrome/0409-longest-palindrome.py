from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic=Counter(s)
        l=0
        odd=0
        
        
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

        