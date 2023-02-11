# URL: https://leetcode.com/problems/product-of-array-except-self

def prodArray(nums):
    res = [1] * len(nums)

    prefix = 1
    # First run to calculate and store the prefix
    for i in range(len(nums)):
        # Taking the prefix and putting it into the position i
        res[i] = prefix
        # Compute the prefix as we iterate over the ip array
        prefix *= nums[i]

    postfix = 1
    # Second run to calculate and store the postfix
    for i in range(len(nums) - 1, -1, -1):
        # Multiply with the value which is already in the array
        res[i] *= postfix
        # Compute the postfix
        postfix *= nums[i]

    return res

    
if __name__ == "__main__":
    nums = [1,2,3,4]
    print(prodArray(nums))
