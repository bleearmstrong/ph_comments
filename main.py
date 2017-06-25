# ben armstrong
# this project will scrape comments from the most popular videos on pornhub
# not sure what to do with them afterwards


from lxml import html
from urllib.request import urlopen
import time
import json

class Scraper:

    def __init__(self, start=1, end=100, wait=5):
        self.start = start
        self.end = end
        self.root = 'https://www.pornhub.com/video?o=mv&cc=us&page='
        self.xpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "title", " " ))]//a'
        self.links = list()
        self.comment_xpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "commentMessage", " " ))]'
        self.comments = list()
        self.wait = wait

    def get_videos(self):

        for i in range(self.start, self.end + 1):
            print('getting page {}'.format(i))
            video_url = self.root + str(i)
            connection = urlopen(video_url)
            dom = html.fromstring(connection.read())
            z = [x for x in dom.xpath(self.xpath)]
            z = [(x.get('href'), x.text) for x in z]
            z = list(set(z))
            self.links.extend(z)

            if i != self.end:
                time.sleep(self.wait)

    def get_comments(self):

        for i, link in enumerate(self.links):
            try:
                title = link[1]
                video = 'https://www.pornhub.com' + link[0]
                print('parsing comments for video: {}'.format(title))
                print('{} links remain'.format(len(self.links) - i))
                connection = urlopen(video)
                dom = html.fromstring(connection.read())
                y = [x.text_content() for x in dom.xpath(self.comment_xpath)]
                y = [str(x).strip('\n\t') for x in y]
                y = [x[:x.index('\n\t')] for x in y]
                output = [(title, video, y)]
                self.comments.extend(output)

                time.sleep(self.wait)
            except:
                print('Video --{}-- failed'.format(title))
                time.sleep(self.wait)

    def to_dict(self):
        return {str(tup[0] + '|' + tup[1]): [item for item in tup[2] if 'commentMessage' not in item]
                for tup in s.comments}

    def to_json(self):
        x = self.to_dict()
        return json.dumps(x)
