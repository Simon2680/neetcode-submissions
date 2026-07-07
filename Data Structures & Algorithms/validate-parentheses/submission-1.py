class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        stack = []

        for char in s:
            if char in ['(','{','[']:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if (top is '(' and char is not ')') or (top is '{' and char is not '}') or ( top is '[' and char is not ']'):
                    return False
        if len(stack) != 0:
            return False
        return True
        