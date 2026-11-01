class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c=0
        l=len(s)
        if l == 0:
            return True
        for i in t:
            if l>c and s[c] == i:
                c+=1
        if c == l:
            return True
        else:
            return False