from Leaderboard import Leaderboard
from Post import Post
import Globals

class LeaderboardCollection:
    def __init__(self, posts : [Post]):
        self.Leaderboards = [Leaderboard(Globals.Labels[i]) for i in range(len(Globals.Labels))]

        for post in posts:
            for result in post.results:
                self.Leaderboards[result.label].addResult(result)