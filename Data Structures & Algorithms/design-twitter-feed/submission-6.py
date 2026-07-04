import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followerMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.followerMap[userId].add(userId)
        for followeeId in self.followerMap[userId]:
            followeeIdList = self.tweetMap[followeeId]
            if followeeIdList: # list actually has smth in it
                index = len(followeeIdList) - 1
                time, tweetId = followeeIdList[index]
                heapq.heappush(heap, [time, tweetId, followeeId, index - 1]) 
        
        while heap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(heap, [time, tweetId, followeeId, index - 1])


        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followerMap[followerId].discard(followeeId)       
