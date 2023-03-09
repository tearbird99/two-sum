def twoSum(nums, target):
    n = list()
    m = list()

    for i in range(len(nums)):
        key = target - nums[i]
        m = nums[i + 1:]
        if key in m:
            n = [i, m.index(key) + i + 1]
            break

    return n
