from collections import defaultdict, deque
import heapq
class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweetmap = defaultdict(deque) #userid and tweetids
        self.followersmap = defaultdict(set) # userd and followees id
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        #add the tweet in the list corresponding to its userid and attach the timestamp on it
        self.timestamp -=1
        self.tweetmap[userId].append((self.timestamp, tweetId))
        if len(self.tweetmap[userId])>10:
            self.tweetmap[userId].popleft()  
        
    def getNewsFeed(self, userId: int) -> List[int]:
        #get all the followees
        alltweets= list(self.tweetmap[userId])
        for followeeId in self.followersmap[userId]:
            #combine all tweets
            if followeeId != userId:
                alltweets.extend(self.tweetmap[followeeId])
            
        heapq.heapify(alltweets)
        res = []
        for _ in range(min(10, len(alltweets))):
            res.append(heapq.heappop(alltweets)[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        #add follow id into its corresponding userid values in followers map
        if followeeId not in self.followersmap[followerId]:
            self.followersmap[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #remove the followee from the set
        if followeeId in self.followersmap[followerId]:
            self.followersmap[followerId].remove(followeeId)

        
