class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = 0

        for i in range(len(a)-1 ,-1,-1):
            num = int(a[i]) - 0
            num = num * (2**(len(a) - i-1))
            sum += num

    
        for i in range(len(b)-1 ,-1,-1):
            num = int(b[i]) - 0
            num = num * (2**(len(b) - i-1))
            sum += num
        
        sum = bin(sum)[2:]
        return str(sum)
