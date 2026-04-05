class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_ana = {}
        for word in strs:
            count =  [0]*26
            for char in word:
                count[ord(char)-ord('a')]+=1
            key = tuple(count)
            if key not in group_ana:
                group_ana[key]=[]
            group_ana[key].append(word) 
        return list(group_ana.values())