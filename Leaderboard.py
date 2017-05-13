from Result import Result
import Globals

class Leaderboard:

    def __init__(self, label : str):
        self.__results = []
        self.isSorted = False
        self.label = label

    def addResult(self, newResult : Result):
        # duplicate/quote check
        for existingResult in self.__results:
            if newResult.string.find(existingResult.string) != -1:
                return # don't add
        self.__results.append(newResult)

    def results(self): # copy
        return self.__results.copy()

    def sort(self, flag : Globals.Order): # in-place
        if flag is Globals.Order.ASCENDING:
            self.__results.sort(key=lambda result: result.keyScore, reverse=False)
        else:
            self.__results.sort(key=lambda result: result.keyScore, reverse=True)

        self.isSorted = True

    def getFormattedLeaderboard(self, format : int):
        if not self.isSorted:
            return None

        outputList = self.__results.copy()

        for i in range(len(outputList)):
            outputList[i].prettify()

        # moramo ohraniti samo najboljši rezultat posameznega uporabnika ?
        if format & Globals.Format.LEADERBOARD:
            i = 0
            while (i < len(outputList)):
                j = i + 1
                while (j < len(outputList)):
                    if outputList[i].nickname == outputList[j].nickname:
                        del outputList[j]
                    else:
                        j += 1
                i += 1

        outputStringList = []
        rank = 1
        for outputElement in outputList:
            outStr = ""
            if format & Globals.Format.NAMED:
                outStr = outputElement.getResultWithNickname()
            else:
                outStr = outputElement.getResult()

            if format & Globals.Format.LEADERBOARD:
                outStr = str(rank) + ". " + outStr

            outputStringList.append(outStr)
            rank += 1

        return outputStringList

    def getFormattedLeaderboardWithLabel(self, format: int):
        return ["<strong>" + self.label + ":</strong>"] + self.getFormattedLeaderboard(format) + ["\n"]