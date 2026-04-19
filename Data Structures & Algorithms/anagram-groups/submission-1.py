class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        create a helper method to find count vector of each word
        return a tuple that will be the key in dictionary
        : values of this dictionary is a list of all word with the same 
          count vector

        create a dictionary that will keep keys as tuple from count vector

        loop through all the words in the list and find its count vector 
        check if that count vector is in my dictionary
          if it is not--> create a key-value pair, where key is count vector
                        and value is the word
          if it is--> append the word on the value list

          in the end return list of all. dictionary values

          edge cases: when list is empty --> return [[""]]




        
        """
        def find_count_vector(word):
            countVector = [0]*26
            for char in word:
                countVector[ord(char)-ord("a")] +=1

            return tuple(countVector)

        if len(strs) == 0:
            return [[""]]
        

        myDict = {}

        for word in strs:
            if find_count_vector(word) not in myDict:
                myDict[find_count_vector(word)] = [word]
            else:
                myDict[find_count_vector(word)].append(word)

        return list(myDict.values())
                

        




        