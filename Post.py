import scrapy
import re
from Result import Result
import Globals

class Post:

    def __init__(self, html : str, rootURL : str):
        self.HTML = html# celoten HTML v postu
        self.isParsed = False # zastavica, ki pove, ce je post prebran
        self.URL = rootURL # URL do posta
        self.results = [] # seznam rezultatov
        self.HTMLselector : scrapy.Selector
        self.nickname : str

        self.parse()

    def __setURL(self):
        postID = self.HTMLselector.xpath('//div/a/@name').extract_first() # dobi ID posta, ki je uporabljen za URL
        self.URL += "/" + postID + "#" + postID

    def __getNickname(self):
        self.nickname = self.HTMLselector.xpath('//h4/a/text()').extract_first()  # dobi ID posta, ki je uporabljen za URL

    def __getResults(self):
        content = self.HTMLselector.xpath('//div[contains(@class, "content")]/descendant-or-self::*').extract_first() # dobi text vsebino posta
        content = re.sub(r'<br>', "\n", content) # zamenjaj HTML line break za string line break
        content = re.sub(r'<.*?>', "", content) # odstrani HTML značke

        lines = content.split('\n')
        lineNumber = 0
        for line in lines:
            data = line.split(Globals.Delim) # split result

            if len(data) > 1:
                try:
                    keyScore = float(data[Globals.KeyScorePosition].replace(',', '.')) # parsaj (glavni) rezultat
                    # make bold
                    data[Globals.KeyScorePosition] = "<strong>" + data[Globals.KeyScorePosition].strip() + "</strong>"

                    label = self.__findLabel(lineNumber, lines)

                    # odstrani hardcodan nickname iz rezultata
                    if Globals.ExpectedNicknamePosition < len(data):
                        del data[Globals.ExpectedNicknamePosition]
                    for i in range(len(data)):
                        if data[i].strip() == self.nickname:
                            del data[i]
                            break

                    result = Result(Globals.Delim.join(data), keyScore, self.nickname, self.URL, label)
                    self.results.append(result)
                except ValueError:
                    pass
                except IndexError:
                    print("INDEX ERROR at post: " + self.URL + " ... napačen input score/nickname index mogoče?")
            lineNumber += 1

        return self.results

    def __findLabel(self, lineNumber : int, lines : [str]):
        lineNumber -= 1
        while(lineNumber >= 0):
            maxIndex = 0
            labelIndex = -1
            for j in range(len(Globals.Labels)):
                foundIndex = lines[lineNumber].lower().rfind(Globals.Labels[j].lower())
                if foundIndex >= maxIndex:
                    maxIndex = foundIndex
                    labelIndex = j
            if labelIndex != -1:
                return labelIndex # vrni najdeno indeks najdene labele
            lineNumber -= 1

        return -1 # nismo našli labele


    # preparsaj nastavljen HTML
    def parse(self):
        self.HTMLselector = scrapy.Selector(text=self.HTML) # html string --> selector
        self.__getNickname()
        self.__setURL()
        return self.__getResults()