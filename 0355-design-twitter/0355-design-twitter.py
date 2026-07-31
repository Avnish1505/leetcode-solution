import collections
import heapq

class Twitter:

    def __init__(self):
        self.count = 0  # Global timestamp tracker
        self.tweetMap = collections.defaultdict(list)  # userId -> list of [count, tweetId]
        self.followMap = collections.defaultdict(set)   # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Latest tweet ko pehle laane ke liye count ko ghata rahe hain (-1, -2, ...)
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        minHeap = []

        # User khud ko bhi follow karta hai (logical convenience)
        self.followMap[userId].add(userId)

        # Har followee ka sabse recent (aakhri) tweet heap mein daalo
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap and self.tweetMap[followeeId]:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                # Heap item: [count, tweetId, followeeId, previous_index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # Top 10 most recent tweets nikaalo
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            # Agar us user ke paas aur purane tweets hain, unhe heap mein push karo
            if index >= 0:
                prev_count, prev_tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [prev_count, prev_tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Khud ko unfollow karne se roko
        if followeeId in self.followMap[followerId] and followerId != followeeId:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)