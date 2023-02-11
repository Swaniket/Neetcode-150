# URL: https://leetcode.com/problems/top-k-frequent-elements/

def topK(nums, k):
    # To count the occerance of the elements
    count = {}
    
    # The indexes -> count of an element and value -> list of values with that count
    freq = [[] for i in range(len(nums) + 1)]

    # Count how many times each value occers in nums
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        # The value n occers c number of times
        freq[c].append(n)

    res = []

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k: 
                return res

    

if __name__ == "__main__":
    nums = [1,1,1,2,2,3] 
    k = 2
    print(topK(nums, k))
