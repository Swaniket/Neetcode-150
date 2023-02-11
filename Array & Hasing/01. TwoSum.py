# URL: https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    valueMap = {}

    for i, value in enumerate(nums):
        diff = target - value

        if diff in list(valueMap.keys()):
            return [valueMap[diff], i]
        else:
            valueMap[value] = i


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target))
