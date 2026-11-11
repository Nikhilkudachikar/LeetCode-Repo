class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s1=s.split("-")
        l=0
        s2="".join(s1).upper()
        c=k
        s2_l=len(s2)
        s4=[]
        while s2:
            s4.append(s2[-k:])
            s2=s2[:-k]
            
        return "-".join(s4[::-1])