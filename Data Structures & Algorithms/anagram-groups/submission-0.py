"""
Understand 
Input- array of strings 
Output - list of lists of anagrams

Map - hashmap 

Plan -  
1. initialize a hashmap 
2. for each element inside strs:
    initialize an array with all 0s
    loop through the characters of element
    add 1 for the letter's position in the array 
    hasmap[array] = list.append(word)
3. return the hashmap values converted to list

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashm = defaultdict(list)
        for str in strs:
            arr = [0] * 26
            for char in str:
                arr[ord(char)-ord("a")] += 1
            hashm[tuple(arr)].append(str)
        return list(hashm.values())




        