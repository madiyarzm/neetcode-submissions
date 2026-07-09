class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def is_number(x):
            try:
                float(x)
                return True
            
            except ValueError:
                return False

        stack = []

        for token in tokens:
            if token == "+":
                operand2 = stack.pop()
                operand1 = stack.pop()

                stack.append(operand1 + operand2)
                
            elif token == "-":
                operand2 = stack.pop()
                operand1 = stack.pop()

                stack.append(operand1 - operand2)
                
            elif token == "*":
                operand2 = stack.pop()
                operand1 = stack.pop()

                stack.append(operand1 * operand2)
                
            elif token == "/":
                operand2 = stack.pop()
                operand1 = stack.pop()

                stack.append(int(operand1 / operand2))

            else:
                stack.append(int(token))
        
        return int(stack[0])