class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = 0
        dic = {}
        for i in range(len(strs)):
            word = ''.join(sorted(strs[i]))
            if word not in dic:
                dic.setdefault(word , [])
                dic[word].append(strs[i])
            else:
                dic[word].append(strs[i]) 
        return dic.values() 
