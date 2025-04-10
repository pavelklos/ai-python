# 253 : Web Scraping [scrape.py]
# - is technique used to extract large amounts of data from websites whereby the data
#   is extracted and saved to local file in your computer or to database in table (spreadsheet) format.

# TODO: [Hacker News] Python Project
# - https://news.ycombinator.com/
#   - build project (tool) using web scraping to find out all stories that have over 100 points
#   - use Beautiful Soup library

# TODO: DOC [Beautiful Soup], [Requests: HTTP for Humans™]
# - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# - https://docs.python-requests.org/en/master/

# TODO: [Set up environment]
# > pip install requests
# > pip install beautifulsoup4

import pprint

# TODO: [import]
import requests
from bs4 import BeautifulSoup

print("Web Scraping by Beautiful Soup")

res = requests.get("https://news.ycombinator.com/news")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
soup = BeautifulSoup(res.text, "html.parser")  # default parser : html.parser
soup2 = BeautifulSoup(res2.text, "html.parser")  # default parser : html.parser
# print(res)                                          # <Response [200]> : 200 means OK
# print(res.text)                                     # HTML content
# print(soup)                                         # HTML content
# print(soup.body)                                    # body content
# print(soup.body.contents)                           # body content in list
# print(soup.find_all('div'))                         # find all div tags
# print(soup.find_all('a'))                           # find all anchor tags
# print(soup.title)                                   # title tag : <title>Hacker News</title>
# print(soup.a)                                       # first anchor tag
# print(soup.find('a'))                               # first anchor tag
# print(soup.find(id='score_42115515'))               # find tag with id 'score_42115515'

# titles = soup.select('.titleline')      # select all tags with class 'titleline'
# scores = soup.select('.score')          # select all tags with class 'score'
# print(titles)                           # all tags with class 'titleline'
# print(titles[0])                        # first tag
# print(titles[0].text)                   # first tag text
# print(scores)                           # all tags with class 'score'
# print(scores[0])                        # first tag
# print(scores[0].text)                   # first tag text

# TODO: .titleline > a
# <span class="titleline">
#     <a href="https://nathangoldwag.wordpress.com/2024/10/26/visualizing-the-past-world-war-ii/">
#         Visualizing World War II
#     </a>

# TODO: .subtext
# <td class="subtext">
#     <span class="subline">
#         <span class="score" id="score_42110588">
#             66 points
#         </span>

# TODO: soup.select() => type  # <class 'bs4.element.ResultSet'>
links = soup.select(".titleline > a")  # heads up! .storylink changed to .titleline
subtext = soup.select(".subtext")
links2 = soup2.select(".titleline > a")  # heads up! .storylink changed to .titleline
subtext2 = soup2.select(".subtext")

mega_links = links + links2
mega_subtext = subtext + subtext2

# print(mega_links)                            # all tags with class 'titleline'
# print(mega_subtext)                          # all tags with class 'subtext'


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()  # 'How I ship projects at big tech companies'
        href = item.get("href", None)  # 'https://www.seangoedecke.com/how-to-ship/'
        vote = subtext[idx].select(".score")  # 1232 points
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_stories_by_votes(hn)


# pprint.pprint(create_custom_hn(links, subtext))
pprint.pprint(create_custom_hn(mega_links, mega_subtext))

# TODO: # UTF-8
# with open("hn-logfile.log", "w", encoding='utf-8') as log_file:
#     pprint.pprint(create_custom_hn(mega_links, mega_subtext), log_file)

# TODO: # UTF-8 with BOM
with open("hn-logfile.log", "w", encoding="utf-8-sig") as log_file:
    pprint.pprint(create_custom_hn(mega_links, mega_subtext), log_file)


# TODO: [scraper.py] UPDATED ---------------------------------------------------
# import requests
# from bs4 import BeautifulSoup
# import pprint
#
# res = requests.get('https://news.ycombinator.com/news')
# res2 = requests.get('https://news.ycombinator.com/news?p=2')
# soup = BeautifulSoup(res.text, 'html.parser')
# soup2 = BeautifulSoup(res2.text, 'html.parser')
#
# links = soup.select('.titleline > a')  # heads up! .storylink changed to .titleline
# subtext = soup.select('.subtext')
# links2 = soup2.select('.titleline > a')  # heads up! .storylink changed to .titleline
# subtext2 = soup2.select('.subtext')
#
# mega_links = links + links2
# mega_subtext = subtext + subtext2
#
#
# def sort_stories_by_votes(hnlist):
#     return sorted(hnlist, key=lambda k: k['votes'], reverse=True)
#
#
# def create_custom_hn(links, subtext):
#     hn = []
#     for idx, item in enumerate(links):
#         title = item.getText()
#         href = item.get('href', None)
#         vote = subtext[idx].select('.score')
#         if len(vote):
#             points = int(vote[0].getText().replace(' points', ''))
#             if points > 99:
#                 hn.append({'title': title, 'link': href, 'votes': points})
#     return sort_stories_by_votes(hn)
#
#
# pprint.pprint(create_custom_hn(mega_links, mega_subtext))


# TODO: [scrape.py] OLD --------------------------------------------------------
# import requests
# from bs4 import BeautifulSoup
# import pprint
#
# res = requests.get('https://news.ycombinator.com/news')
# res2 = requests.get('https://news.ycombinator.com/news?p=2')
# soup = BeautifulSoup(res.text, 'html.parser')
# soup2 = BeautifulSoup(res2.text, 'html.parser')
#
# links = soup.select('.storylink')
# subtext = soup.select('.subtext')
# links2 = soup2.select('.storylink')
# subtext2 = soup2.select('.subtext')
#
# print(links)
#
# mega_links = links + links2
# mega_subtext = subtext + subtext2
#
#
# def sort_stories_by_votes(hnlist):
#     return sorted(hnlist, key=lambda k: k['votes'], reverse=True)
#
#
# def create_custom_hn(links, subtext):
#     hn = []
#     for idx, item in enumerate(links):
#         title = item.getText()
#         href = item.get('href', None)
#         vote = subtext[idx].select('.score')
#         if len(vote):
#             points = int(vote[0].getText().replace(' points', ''))
#             if points > 99:
#                 hn.append({'title': title, 'link': href, 'votes': points})
#     return sort_stories_by_votes(hn)
#
# # pprint.pprint(create_custom_hn(mega_links, mega_subtext))
