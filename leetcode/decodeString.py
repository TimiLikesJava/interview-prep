class Solution:
    def decodeString(self, s: str) -> str:
        cnum= 0
        stack = []
        message = ''
        for i in s:
            if i == '[':
                stack.append(cnum)
                stack.append(message)
                cnum = 0
                message = ''
            elif i == ']':
                p_message = stack.pop()
                num = stack.pop()
                message = p_message + message*num
            elif i.isdigit():
                cnum = cnum * 10 + int(i)
            else:
                message += i
        return message
