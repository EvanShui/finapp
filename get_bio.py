from bs4 import BeautifulSoup
import sys
import urllib.request

import re
import constants

def render(source_html):
    """Fully render HTML, JavaScript and all."""

    from PyQt5.QtCore import QEventLoop
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtWebEngineWidgets import QWebEngineView

    class Render(QWebEngineView):
        def __init__(self, html):
            self.html = None
            self.app = QApplication(sys.argv)
            QWebEngineView.__init__(self)
            self.loadFinished.connect(self._loadFinished)
            self.setHtml(html)
            while self.html is None:
                self.app.processEvents(QEventLoop.ExcludeUserInputEvents | QEventLoop.ExcludeSocketNotifiers | QEventLoop.WaitForMoreEvents)
            self.app.quit()

        def _callable(self, data):
            self.html = data

        def _loadFinished(self, result):
            self.page().toHtml(self._callable)

    return Render(source_html).html


def bio_scraper(tick):

    from selenium import webdriver
    browser = webdriver.Chrome("C:/Users/eshui/Downloads/chromedriver_win32/chromedriver.exe")
    url = constants.yahoo_bio_url
    browser.get(url)

    html = browser.execute_script("return document.body.innerHTML")
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.find_all('div', {'class': 'quote-section'}))

'''
    url = constants.yahoo_bio_url
    url = constants.yahoo_bio_url
    client_response = Client(url)
    source = client_response.mainFrame().toHtml()

    soup = BeautifulSoup(source, 'lxml')
    js_test = soup.find('p', class_ = 'jstest')

    print(len(soup.find_all('div')))
    print(len(soup.find_all('div', {'class':'quote-section'})))
    print(len(soup.find_all('div', {'class':'sticky-inner-wrapper'})))

    print(len(soup.find_all('div', {'quote':'quote-mdl'})))

    print(soup.find_all('div', {'data-reactid':'33'}))


    soup = BeautifulSoup(page.content, 'html.parser')
    print(len(soup.find_all('div')))
    print(len(soup.find_all('div', {'class':'quote-section'})))
    print(len(soup.find_all('div', {'class':'sticky-inner-wrapper'})))
    print(len(soup.find_all('div', {'quote':'quote-mdl'})))
    print(len(soup.find_all('div', {'data-reactid':'2'})))
    print(soup.find_all('div', {'data-reactid':'33'}))

    for p in (soup.find_all('div', attrs={'class':'quote-section'})):
        print(p)
    # print(soup.find('p', {'class':'businessSummary'}))
'''

if __name__ == '__main__':
    bio_scraper('msft')

