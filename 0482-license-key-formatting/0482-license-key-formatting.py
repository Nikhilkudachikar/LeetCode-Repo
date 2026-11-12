class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s2=s.replace("-","").upper()
        s4=[]
        while s2:
            s4.append(s2[-k:])
            s2=s2[:-k]
            
        return "-".join(s4[::-1])