def twoSum(self, nums: List[int], target: int) -> List[int]:
    ans = list()

    for i in range(len(nums)):
        if target - nums[i] in nums:
            ans = [nums.index(target - nums[i]), i]

    return ans
