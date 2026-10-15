class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s1={}
        c=0
        for i in s:
            if i in s1:
                if s1[i]!=t[c]:
                    return False
            else:
                if t[c] in list(s1.values()):
                    if i in s1:
                        if s1[i]!=t[c]:
                            return False
                    else:
                        return False
                s1[i]=t[c]
            c+=1
        return True
s=Solution()
print(s.isIsomorphic(s = "title", t = "paper"))
