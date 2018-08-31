import urllib.request
from bs4 import BeautifulSoup
import re
import constants

def web_scraper(tick, day, month, year):
    lst = []
    opener = urllib.request.build_opener()
    url = (constants.marketwatch_url.format(ticker=str(tick).upper(), month=str(month), day=str(day), year=str(year)))

    page = opener.open(url)
    soup = BeautifulSoup(page, "html.parser")

    soup_tuple_list = zip(soup.findAll(class_="searchresult"), soup.findAll(class_="deemphasized")[1:-1])

    for article, date in soup_tuple_list:
        try:
            lst.append(return_article_info(article, date))
        except:
            continue
    return lst

def return_article_info(article, date):
    ret = {}
    time = date.contents[0].contents[0]
    ret['time'] = str(date.contents[0].contents[0])
    ret['author'] = re.findall(r'(?<=\|\ )(.*)', date.contents[1])[0].rstrip()
    ret['article_bio'] = str(article.a.contents[0])
    ret['article_link'] = str(article.a['href'])
    return ret


if __name__ == '__main__':
    # testing
    for article in web_scraper('NFLX', 10, 12, 2007):
        print(article)
     
