from collections import defaultdict
import heapq as h
class Twitter(object):

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        self.count = 0
        
    def postTweet(self, userId, tweetId):
        self.tweet_map[userId].append((self.count, tweetId))

        # decrement count instead of incremeneting, because we want a 
        # max-heap but Python heap is a min-heap
        self.count -= 1
        

    def getNewsFeed(self, userId):
        max_heap = list(self.tweet_map[userId])

        for followeeId in self.follow_map[userId]:
            max_heap += self.tweet_map[followeeId]

        L = len(max_heap)
    
        h.heapify(max_heap)
        return [h.heappop(max_heap)[1] for _ in range(min(10, L))]

        # alternate approach

        # max_heap.sort()
        # return [max_heap[i][1] for i in range(min(10, L))]

    def follow(self, followerId, followeeId ) :
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        self.follow_map[followerId].discard(followeeId)
        
twitter = Twitter()
twitter.postTweet(1, 5) #// User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1)  #;  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2)    #;    // User 1 follows user 2.
twitter.postTweet(2, 6) #; // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1)  #;  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2)  #;  // User 1 unfollows user 2.
twitter.getNewsFeed(1)  