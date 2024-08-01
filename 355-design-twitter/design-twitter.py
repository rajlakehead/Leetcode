class Twitter:

    def __init__(self):
        self.userfollowlist = defaultdict(set)
        self.feed = collections.deque()
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for news in reversed(self.feed):
            if news[0] in self.userfollowlist[userId] or userId == news[0]:
                res.append(news[1])
            if len(res) >= 10:
                break
        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userfollowlist[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userfollowlist[followerId]:
            self.userfollowlist[followerId].remove(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)