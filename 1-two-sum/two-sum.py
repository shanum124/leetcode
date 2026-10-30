class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ma = {}
        for i in range(len(nums)):
            if nums[i] in ma:
                return [ma[nums[i]], i]
            ma[target-nums[i]] = i
        # for key, value in ma.items():
        #     ke = ma.get(value)
        #     if ke is not None:
        #         print(value, ke)
        #         if key==value
        #         x = nums.index(key)
        #         y = nums.index(value)
        #         if x!=y:
        #             return [x, y]  
        # return [-1]