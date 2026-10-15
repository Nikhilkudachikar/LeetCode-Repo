class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l=s.split()
        if len(pattern)!=len(l):
            return False
        s2={}
        c=0
        for i in pattern:
            if i in s2:
                if s2[i]!=l[c]:
                    return False
            else:
                if l[c] in list(s2.values()):
                    if i in s2:
                        if s[i]!=l[c]:
                            return False
                    else:
                        return False
                            
                s2[i]=l[c]
            c+=1
        return True

