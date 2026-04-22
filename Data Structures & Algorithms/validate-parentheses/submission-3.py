class Solution:
    def isValid(self, s: str) -> bool:
        """
        U: return true if the tags are balanced and false otherwise
        P: create a dictionary that keeps tags as the keys
        create empty stack
           loop through the entire string and once you find the opening tag, add it to the stack
           once you find closing tag see if there is it's corresponding opening tag
           on the tail of our stack
             if it is there:
                  remove it from the stack
            
            if the tag on the tail is not its corresponding 
            return false

            if the tag is opening:
                add it to the stack
        """

        myStack = []
        myDict = {"}":"{", ")":"(", "]":"["}
        for char in s:
            if char in "[({":
                myStack.append(char)
            if char in "})]":
                if myStack and myStack[-1] == myDict[char]:
                    myStack.pop()
                else:
                    return False
        return len(myStack) == 0
        