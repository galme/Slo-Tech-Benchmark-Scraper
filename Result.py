import Globals

class Result:
    def __init__(self, string : str, score : float, nick : str, url : str, label : int):
        self.string = string
        self.keyScore = score
        self.nickname = nick
        self.URL = url
        self.label = label

    def getResultWithNickname(self):
        return "<strong>" + self.nickname + "</strong>" + " " + Globals.Delim + " " + self.getResult()

    def getResult(self):
        return self.string.strip() + " " + Globals.Delim + " <a href=\"" + self.URL + "\">link</a>"

    def prettify(self): # da so presledki ok ... in place
        self.data = self.string.split(Globals.Delim)
        for i in range(len(self.data)):
            self.data[i] = " " + self.data[i].strip() + " "

        self.string = Globals.Delim.join(self.data)

    def __str__(self):
        return "REZULTAT:\nstring: " + self.string + "\nscore: " + str(self.keyScore) + "\nnick: " + self.nickname + "\n-----------------"
