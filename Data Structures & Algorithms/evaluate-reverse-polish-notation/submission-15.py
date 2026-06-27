class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        helper method to convert operator or operand into an inetger or operand
        ######################################################################
        operate(operand1, operand2, operator):
          if operand1 or operand2 = "string":
            operand1 or operand2 = corresponding int

        if operator = "operator":
            return operand1 operator operand2



        create an empty stack
        create a for loop:
        move until you hit the operator:
          then check what is in the stack:
            if stack empty-->use the sign between two numbers:

                i operator i+1
                push the result on the stack
            if stack is not empty:
                i operator then pop in the stack
                push the result in the stack
            return pop from the stack
        """

        def operate(operand1, operand2, operator):
            if operator == '+':
                return operand1 + operand2
            elif operator == '-':
                return operand1 - operand2
            elif operator == '*':
                return operand1 * operand2
            else:
                return int(operand1/operand2)


        stack = []
        operators = ['+', '-', '*', '/']
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(int(operate(int(operand1), int(operand2), tokens[i])))
            
        return int(stack.pop())
