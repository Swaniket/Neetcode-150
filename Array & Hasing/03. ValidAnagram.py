# URL: https://leetcode.com/problems/valid-anagram/

# The hashmap solution:
# Time: O(s+t), Space: O(s+t)

# The Sorting Solution:
# Time: Depends of sorting algorithm O(nlogn) 
# Space: Depends on the sorting algorithm O(n) or O(1) 

def validAnagram(s, t):
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}

    for i in range(len(s)):
        # Everytime we see a character, increment the count by 1
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    # Iterate over the hasmap to see if the counts are the same
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True


def validAnagramBySort(s, t):
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(validAnagram(s, t))
    print(validAnagramBySort(s, t))
