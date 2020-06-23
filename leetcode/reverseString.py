class Solution:
    def reverseString(self, s: List[str]) -> None:
        j = len(s) - 1
        for i in range(len(s)):
            if(j < i):
                break
            if(i == j):
                break
            s[i] , s[j] = s[j] , s[i]
            j -= 1
        return s
