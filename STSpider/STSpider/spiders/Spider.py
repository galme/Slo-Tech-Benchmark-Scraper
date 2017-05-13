import scrapy
from Post import Post
from LeaderboardCollection import LeaderboardCollection
import Globals

class Spider(scrapy.Spider):
    name = "Spider"
    posts = []

    def start_requests(self):
        URL = getattr(self, 'URL', None)
        if URL is not None:
            yield scrapy.Request(URL, self.parse)
        else:
            yield None

    # parsaj response
    def parse(self, response : scrapy.Selector):
        # for each post
        for postHTML in response.css('div.post').extract():
            post = Post(postHTML, response.url)
            self.posts.append(post)

        # pojdi na naslednjo stran (in tam ponovi celoten postopek)
        yield self.goToNextPage(response)

    def goToNextPage(self, response):
        nextPage = response.xpath('//span[contains(@class, "pages")]/a[contains(@rel, "next")]/@href').extract_first() # >> "gumbek" z linkom za naslednjo stran
        if nextPage is not None:
            nextPage = response.urljoin(nextPage)
            return scrapy.Request(nextPage, self.parse)
        else:
            self.spiderDone()

    def spiderDone(self):
        leaderboardCollection = LeaderboardCollection(self.posts)
        leaderboardCollection.writeToFile()