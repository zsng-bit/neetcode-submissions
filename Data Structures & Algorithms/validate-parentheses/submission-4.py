class Solution:
    def isValid(self, s: str) -> bool:
        op = []
        for i in s:
            if i == '{':
                op.append('curl')
            elif i == '(':
                op.append('reg')
            elif i == '[':
                op.append('brack')

            if len(op) == 0:
                return False
            elif i == ')':
                if op.pop() == 'reg':
                    continue
                else:
                    return False
            elif i == '}':
                if op.pop() == 'curl':
                    continue
                else:
                    return False
            elif i == ']':
                if op.pop() == 'brack':
                    continue
                else:
                    return False
        if len(op) == 0:
            return True
        else:
            return False


   
        