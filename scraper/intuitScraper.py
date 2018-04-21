import requests
from articleScraper import scrapeArticle
from bs4 import BeautifulSoup
import csv

filename = 'answers.csv'
intuit_url = 'https://accountants-community.intuit.com'

f = csv.writer(open(filename, 'wb'))

data = open(filename, 'w')

headers = 'title, url, upvotes, lastModifiedtime, lastModifiedText, content\n'

data.write(headers)

for i in range(100):
    site = 'https://accountants-community.intuit.com/search?filters%5Bproduct_name%5D=ProConnect+Tax+Online&filters%5Bproduct_platform%5D=&page=' + str(i) + '&Online&q=%2A%3A%2A'
    page = requests.get(site)
    # https://accountants-community.intuit.com/search?filters%5Bcountry%5D=US&filters%5Bproduct_display_name%5D=ProConnect+Tax+Online&filters%5Bproduct_display_platform%5D=Online&filters%5Btags%5D=&page=2&q=%2A%3A%2A
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find('div', {'id': 'search-results'})
    lists = div.findAll('li', {'class': 'clickable post-item'})


    for list in lists:
        title = list.find('a', {'class': 'post-subject'}).text
        answer = intuit_url + list.find('a', {'class': 'post-subject'})['href']
        lastModifiedtime = scrapeArticle(answer)[0]
        modifiedTimeText = scrapeArticle(answer)[1]
        numOfUpvotes = scrapeArticle(answer)[2]
        main = scrapeArticle(answer)[3]
        print('title: ' + title + ' \nurl: ' + answer + '\nmain: ' + main + '\nnumOfUpVotes' + numOfUpvotes+ '\nlastModifiedTime: ' + str(lastModifiedtime))
        f.writerow([title, answer, numOfUpvotes, lastModifiedtime, modifiedTimeText, main.replace(u'\xa0', ' ').encode('utf-8')])
        # f.write(title + ',' + answer + ',' + main.replace(u'\xa0', ' ').encode('utf-8') + ',' + numOfUpvotes + ',' + lastModifiedtime + '\n')
        # f.write(title + ',' + answer + ',' + main + ',' + numOfUpvotes + ',' + lastModifiedtime + '\n')
        # f.write(title + ',' + answer + '\n')
