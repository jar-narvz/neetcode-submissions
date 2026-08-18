class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}

        for i, nums in enumerate(nums):
            difference = target - nums
            if difference in hash:
                return [hash[difference], i]
            hash[nums] = i

        