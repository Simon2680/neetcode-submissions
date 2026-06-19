
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = Counter(nums)
        sortedDict = dict(sorted(mydict.items(), key=lambda item: item[1], reverse = True))
        res = list(sortedDict.keys())
        return res[:k]
        

        # # use a dictionary to keep number and the times it appear
        #  """
        #  loop through the list:
        #  if number at i is not in the dict add it there and value = 1
        #  if it was there --> value++
        #  sort mydictionary using keys descending
        #  return the first k keys
        #  """
        
        #  myDict = {}
        #  for i in range(len(nums)):
        #     if nums[i] not in myDict:
        #         myDict[nums[i]] = 1
        #     else:
        #         myDict[nums[i]] +=1
         
        #  sortedKeys = sorted(myDict, key=myDict.get, reverse=True)
        #  return sortedKeys[0:k]
        # """
        # use hashmap
        # get the list of all the values in hasmap
        # order them
        # the look for the keys of of the first k values in the dictionary
        # """


        
        
        
        



        