class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2!=0 and high%2!=0:
            return int(((high-low)/2)+1)
        elif low%2==0 and high%2==0:
            return int(((high-low)/2))
        elif (high-low)==1:
            return int((high-low))
        else:
            return int(((high-low)/2)+1)


        