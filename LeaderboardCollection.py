from Leaderboard import Leaderboard
from Post import Post
import Globals
import os

class LeaderboardCollection:
    def __init__(self, posts : [Post]):
        self.Leaderboards = [Leaderboard(Globals.Labels[i]) for i in range(len(Globals.Labels))]

        for post in posts:
            for result in post.results:
                self.Leaderboards[result.label].addResult(result)

    def writeToFile(self):
        # make folder
        if not os.path.exists(os.path.dirname(Globals.FileName)):
            try:
                os.makedirs(os.path.dirname(Globals.FileName))
            except OSError as exc:
                print("OSError pri ustvarjanju izhodne datoteke...")

        text_file = open(Globals.FileName, "w")
        for leaderboard in self.Leaderboards:
            leaderboard.sort(Globals.OutputOrder)
            list = leaderboard.getFormattedLeaderboardWithLabel(Globals.OutputFormat)
            for result in list:
                text_file.write(result + "\n")

        text_file.close()