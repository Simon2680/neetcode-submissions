class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = list(s)
        list2 = list(t)
        if (len(list1) == len(list2)):
            for i in range(len(list1)):
                if (list1[i] in list2 ):
                    list2.remove(list1[i])

    

        
        return len(list2)==0

        