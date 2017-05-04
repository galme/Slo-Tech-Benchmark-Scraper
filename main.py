import Globals
import argparse
from scrapy.crawler import CrawlerProcess
from STSpider.STSpider.spiders.Spider import Spider

# argument definitions
argParser = argparse.ArgumentParser(description='Pregleda dan URL in vse naslednje strani ter generira lestvico.')
argParser.add_argument("-URL", help="URL strani, ki jo skripta naj pregleda", type=str, required=True)
argParser.add_argument("-scoreindex", help="indeks rezultata v formuli ... (default: -1 (zadnje mesto))", type=str, required=False)
argParser.add_argument("-nicknameposition", help="pricakovan indeks vzdevka uporabnika v formuli ... (default: avtomatska zaznava)", type=str, required=False)
argParser.add_argument("-outputformat", nargs='+', help="format izpisa v datoteko. Moznost kombinacije. (default: LEADERBOARD NAMED)", choices=['LEADERBOARD', 'LIST', 'NAMED', 'ANONYMOUS'], type=str, required=False)
argParser.add_argument("-outputorder", help="naraščajoči ali padajoči vrstni red glede na rezultat (default: DESCENDING)", choices=['DESCENDING', 'ASCENDING'], type=str, required=False)
argParser.add_argument("-labels", nargs='*', help="labele, ki predstavljajo imena lestvic (npr. \"1080p, 4K\") (default: Unnamed", type=str)
argParser.add_argument("-out", help="ime izhodne datoteke (default: lestvica.txt)", type=str)
argParser.add_argument("-delimiter", help="znak, ki predstavlja ločnico v formuli rezulatov (default: '|')", type=str)
args = argParser.parse_args()

# argument application
if args.labels is not None:
    Globals.Labels = args.labels + ["Unnamed"]
if args.delimiter is not None:
    Globals.delim = args.delimiter
if args.out is not None:
    Globals.FileName = args.out
if args.scoreindex is not None:
    Globals.keyScorePosition = args.scoreindex
if args.nicknameposition is not None:
    Globals.expectedNicknamePosition = args.nicknameposition
if args.outputformat is not None:
    num = 0
    for el in args.outputformat:
        if el == "LEADERBOARD":
            num |= Globals.Format.LEADERBOARD
        if el == "ANONYMOUS":
            num |= Globals.Format.ANONYMOUS
        if el == "NAMED":
            num |= Globals.Format.NAMED
        if el == "LIST":
            num |= Globals.Format.LIST
    Globals.OutputFormat = num
if args.outputorder is not None:
    if args.outputorder == "ASCENDING":
        Globals.OutputOrder = Globals.Order.ASCENDING
    if args.outputorder == "DESCENDING":
        Globals.OutputOrder = Globals.Order.DESCENDING

# start crawler
process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})
process.crawl(Spider, URL=args.URL)
process.start()