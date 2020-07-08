class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+" , "-" , "/" ,"*"]
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                y = int(stack.pop())
                x = int(stack.pop())
                if(i == '+'):
                    stack.append(x + y)
                elif(i == '-'):
                    stack.append(x-y)
                elif(i == '/'):
                    if x*y < 0 and x % y != 0:
                        stack.append(x//y+1)
                    else:
                        stack.append(x//y)
                else:
                    stack.append(x*y)
        return stack[-1]
