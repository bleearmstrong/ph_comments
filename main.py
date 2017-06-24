# ben armstrong
# this project will scrape comments from the most popular videos on pornhub
# after the comments are scraped, a twitter bot will post them randomly


from lxml import html
import requests

class Scraper:

    def __init__(self, start=1, end=100):
        self.start = start
        self.end = end
        self.root = 'https://www.pornhub.com/video?o=mv&cc=us&page='
        self.xpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "title", " " ))]//a'

    def scrape(self):

        for i in range(start, end + 1):
