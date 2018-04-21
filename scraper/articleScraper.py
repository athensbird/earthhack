import requests
from datetime import datetime
from bs4 import BeautifulSoup

# date_posted = '2014-01-15T01:35:30.314Z'
# datetime.strptime(date_posted, '%Y-%m-%dT%H:%M:%S.%fZ')
# 2018-04-05T02:34:11Z

def scrapeArticle(url):
    currentTime = datetime.now()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    lastModifiedtime = soup.find('time', {'class': 'moment'})['data-timestamp']
    convertedModifiedTime = datetime.strptime(lastModifiedtime, '%Y-%m-%dT%H:%M:%SZ')
    timeDifference = currentTime - convertedModifiedTime
    modifiedTimeText = 'Last Modified ' + str(timeDifference).split(",")[0] + ' ago'

    upvoteList = soup.find('ul', {'class': 'list-unstyled small text-muted mb-2'})
    numOfUpvotes = upvoteList.findAll('li')[1].text.strip().split(" ")[0] if (upvoteList.findAll('li')[1].text) else '0'

    main = soup.find('div', {'class': 'article-body salesforce'}).get_text().strip()

    return convertedModifiedTime, modifiedTimeText, numOfUpvotes, main
