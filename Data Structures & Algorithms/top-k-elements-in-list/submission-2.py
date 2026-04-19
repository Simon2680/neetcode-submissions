class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a dictionary to keep number and the times it appear
         """
         loop through the list:
         if number at i is not in the dict add it there and value = 1
         if it was there --> value++
         sort mydictionary using keys descending
         return the first k keys
         """
        
         myDict = {}
         for i in range(len(nums)):
            if nums[i] not in myDict:
                myDict[nums[i]] = 1
            else:
                myDict[nums[i]] +=1
         

         

         sortedKeys = sorted(myDict, key=myDict.get, reverse=True)
         return sortedKeys[0:k]

         