# ben armstrong
# this project will scrape comments from the most popular videos on pornhub
# after the comments are scraped, a twitter bot will post them randomly


from lxml import html
from urllib.request import urlopen
import time

class Scraper:

    def __init__(self, start=1, end=100):
        self.start = start
        self.end = end
        self.root = 'https://www.pornhub.com/video?o=mv&cc=us&page='
        self.xpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "title", " " ))]//a'
        self.links = list()

    def get_videos(self):

        for i in range(self.start, self.end + 1):
            video_url = self.root + str(i)
            connection = urlopen(video_url)
            dom = html.fromstring(connection.read())
            z = [x for x in dom.xpath(self.xpath)]
            z = [(z.get('href'), z.text) for z in z]
            z = list(set(z))
            self.links.extend(z)

            if i != self.end:
                time.sleep(3)