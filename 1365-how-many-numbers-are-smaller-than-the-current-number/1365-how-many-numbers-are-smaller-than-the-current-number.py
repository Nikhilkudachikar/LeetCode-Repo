class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        greater_nums=[]
        for i in nums:
            c=0
            for j in range(len(nums)):
                if i>nums[j]:
                    c+=1
            greater_nums.append(c)
        return greater_nums    