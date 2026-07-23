class Twitter:
    class TweetNode:
        def __init__(self, tweetId:int, timeStamp:int, nxt:'TreeNode'):
            self.tweetId = tweetId
            self.timestamp = timeStamp
            self.nxt = nxt

    def __init__(self):
        self.follower_to_followee = defaultdict(set) # {followerID:(followee1ID, followee2ID)}
        self.users_post = {} #{userid: Node}
        self._globalTime = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # get the user's tweets linked list
        tweets = self.users_post.get(userId, None)
        newTweet = self.TweetNode(tweetId, self._globalTime, tweets)
        self.users_post[userId] = newTweet
        self._globalTime += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        possible_tweets = [self.users_post.get(userId, None)] 
        followees = self.follower_to_followee.get(userId, None)
        if followees:           
            possible_tweets += [self.users_post.get(followee_id, None) for followee_id in followees]
        
        maxHeap = [] # (-timestamp, tweetId, tweetnode)
        for tweetnode in possible_tweets:
            if tweetnode:
                heapq.heappush(maxHeap, (-tweetnode.timestamp, tweetnode.tweetId, tweetnode))

        k = 10
        topNews = []
        while maxHeap and k > 0:
            popped_tweet = heapq.heappop(maxHeap)[2]
            topNews.append(popped_tweet.tweetId)
            next_tweet = popped_tweet.nxt
            if next_tweet:
                heapq.heappush(maxHeap, (-next_tweet.timestamp, next_tweet.tweetId, next_tweet))
            k -= 1
        return topNews

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            followees = self.follower_to_followee.get(followerId, set())
            followees.add(followeeId)
            self.follower_to_followee[followerId] = followees

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followees = self.follower_to_followee.get(followerId, set())
        if followeeId in followees:
            followees.remove(followeeId)
        self.follower_to_followee[followerId] = followees
        
