class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        g=[]
        for i in nums:
            c=0
            for j in range(len(nums)):
                if i>nums[j]:
                    c+=1
            g.append(c)
        return g