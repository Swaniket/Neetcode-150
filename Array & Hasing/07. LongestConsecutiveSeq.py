# URL: https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutive(nums):
    numSet = set(nums)
    longestSeq = 0

    for n in nums:
        # Check if its a start of a seq
        if (n-1) not in numSet:
            length = 0
            # Check if consecutive number exists in the set.
            while (n+length) in numSet:
                # If it exists, we keep increasing the length
                length += 1
            longestSeq = max(length, longestSeq)

    return longestSeq

if __name__ =="__main__":
    nums = [100,4,200,1,3,2]
    print(longestConsecutive(nums))