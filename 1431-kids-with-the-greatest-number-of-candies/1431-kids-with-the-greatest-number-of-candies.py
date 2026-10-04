class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        show=[]
        for i in candies:
            if i+extraCandies>=max(candies):
                show.append(True)
            else:
                show.append(False)
        return show
        