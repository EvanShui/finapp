import urllib.request
from bs4 import BeautifulSoup
import re
import constants

def web_scraper(day, month, year, tick):
    lst = []
    opener = urllib.request.build_opener()
    url = (constants.marketwatch_url.format(ticker=str(tick).upper(), month=str(month), day=str(day), year=str(year)))

    page = opener.open(url)
    soup = BeautifulSoup(page, "html.parser")

    soup_tuple_list = zip(soup.findAll(class_="searchresult"), soup.findAll(class_="deemphasized")[1:-1])

    for article, date in soup_tuple_list:
        ret = {}
        ret['time'] = date.contents[0].contents[0]
        ret['author'] = re.findall(r'(?<=\|\ )(.*)', date.contents[1])[0].rstrip()
        ret['article_bio'] = article.a.contents[0]
        ret['article_link'] = article.a['href']
        lst.append(ret)
    return lst

if __name__ == '__main__':
    for article in web_scraper(10, 12, '07', 'NFLX'):
        print(article)
     
