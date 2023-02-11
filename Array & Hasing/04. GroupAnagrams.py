# URL: https://leetcode.com/problems/group-anagrams/
from collections import defaultdict

def groupAnagrams(strs):
    # The dict is created with the values as List
    hMap = defaultdict(list) 

    for word in strs:
        count = [0] * 26

        # Counting occerance of each character in every word. It's used for the key.
        for char in word:
            count[ord(char) - ord("a")] += 1

        # Appening the word to it's corrosponding key
        hMap[tuple(count)].append(word)

    return hMap.values()
    

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))
