class Solution:
    def isValid(self, s: str) -> bool:
        
        pars = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for i in range(len(s)):
            if s[i] == ')' or s[i] == '}' or s[i] == ']':
                
                if len(stack) == 0 or pars[stack[-1]] != s[i]:
                    return False
                
                else:
                    stack.pop()
                    continue
                
            stack.append(s[i])
        
        return len(stack) == 0
            