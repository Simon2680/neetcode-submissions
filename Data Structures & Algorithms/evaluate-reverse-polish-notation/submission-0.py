class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char in ['+', '-', '*', '/']:
                rgt = stack.pop()
                lft = stack.pop()

                if char == '+':
                    stack.append(lft + rgt)
                elif char == '-':
                    stack.append(lft - rgt)
                elif char == '*':
                    stack.append(lft * rgt)
                else:
                    stack.append(int(lft / rgt))
            else:
                stack.append(int(char))
        return stack[0]
