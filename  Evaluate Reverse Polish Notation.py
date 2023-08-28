def evalRPN(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        opSet = ('+', '-', "*", '/')
        stack = []
        for val in tokens:
            if val not in opSet:
                stack.append(int(val))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if val == '/':
                    stack.append(int(float(num2)/num1))
                elif val == '-':
                    stack.append(num2 - num1)
                elif val == '*':
                    stack.append(num2 * num1)
                else:
                    stack.append(num2 + num1)


        return stack.pop()

tokens = ["4","13","5","/","+"] #["2","1","+","3","*"]
evalRPN(tokens)