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

        #         [(simon)]
        # """
        # create a stack that will keep the opening tags
        # create a hasmap that will be able to match opening and closing tags
        # create a for loop that will track character that we are at
        # first check if the character is a tag 

        #   check if the tag is in hasmap:
        #      if hasmap[tag] == stck[-1]--> pop from stack

        #      else: treturn False
        #   if the tag not in hasmap:
        #     append it there

        # return len(stack) == 0

        # """
        

        stck = []
        hasmap = {"]":"[", "}":"{", ")":"("}
        for i in range(len(s)):
            if s[i] in ['(', ')', '{', '}','[', ']']:
                # if it is a closing bracket
                if s[i] in hasmap:
                    if stck and hasmap[s[i]] == stck[-1]:
                        stck.pop()
                    else:
                        return False
                else:
                    stck.append(s[i])
        return len(stck) ==0

            

      






        
        

                


               