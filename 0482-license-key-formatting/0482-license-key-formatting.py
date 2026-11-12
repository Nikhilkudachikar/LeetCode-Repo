class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s2=s.replace("-","").upper()
        if k==1:
            return "-".join(s2)
        l=len(s2)
        first=l%k or k
        s4=[s2[:first]]
        for ind in range(first,l,k):
            s4.append(s2[ind:ind+k])
        return "-".join(s4)