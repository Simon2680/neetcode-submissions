from collections import Counter
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

        #   edge cases: when list is empty --> return [[""]]




        
        # """
        # def find_count_vector(word):
        #     countVector = [0]*26
        #     for char in word:
        #         countVector[ord(char)-ord("a")] +=1

        #     return tuple(countVector)

        # #if len(strs) == 0:
        #     #return [[""]]
        

        # myDict = {}

        # for word in strs:
        #     if find_count_vector(word) not in myDict:
        #         myDict[find_count_vector(word)] = [word]
        #     else:
        #         myDict[find_count_vector(word)].append(word)

        # return list(myDict.values())
        #use a hashmap
        # create a helper method to find a hashmap of a word

        # use apointer to track when u are still in the same anagram

        # def count_vector(word):
        #     lst = [0]*26
        #     for i in range(len(word)):
        #         lst[ord(word[i])-ord('a')] += 1
            
        #     return tuple(lst)
        # hasmap = {}
        # for i in range(len(strs)):
        #     if count_vector(strs[i]) not in hasmap:
        #         hasmap[count_vector(strs[i])] = [strs[i]]
        #     else:
        #         hasmap[count_vector(strs[i])].append(strs[i])
        # return list(hasmap.values())

        # red = defaultdict(list)
        # for word in strs:
        #     sortedS = "".join(sorted(word))
        #     red[sortedS].append(word)
        # return list(red.values())
        """
        have an empty dictionary
        use the loop to loop through the list:
           sort the word --> sortedword
           check if sortedkey is on the dictionary
           if it is there:
              --> append the word to the values of that key
          if it is not there:
             ----> create a key : sortedword of that word and put the value as that word
        return list(values of the dictionary)
           
        """

        myDict = {}
        for i in range(len(strs)):
          word = strs[i]
          Sword = tuple(sorted(word))
          if Sword not in myDict:
            myDict[Sword] = [word]
          else:
            myDict[Sword].append(word)
        return list(myDict.values())



    
            




            

            
        
        

                

        




        