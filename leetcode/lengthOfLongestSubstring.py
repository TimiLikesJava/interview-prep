class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num = 0
        mem = set()
        
        i , j = 0 , 0
        
        while(i < len(s) and j < len(s)):
            if(s[j] not in mem):
                mem.add(s[j])
                j += 1
                num = max(num , j-i)
                
            else:
                mem.remove(s[i])
                i += 1
                
        return num
