import requests
from bs4 import BeautifulSoup
import json
from datetime import *
import json 

news=[]
keywords = [
  'corona',
  'covid',
  'brazil'
  'china',
  'chinese'
  'cdc',
  'disease',
  'fda',
  'outbreak',
  'pandemic',
  'virus',
  'who',
]

def rollout(target):
  today = date.today()
  while (target < today):
    get_news(target)
    target = target + timedelta(days = 1)

def get_news(target):
  link_date = target.strftime('%Y/%B/') + f'{target.day}/'
  source = 'https://www.cnbc.com/site-map/' + link_date
  className = 'SiteMapArticleList-link'
  page = requests.get(source)
  soup = BeautifulSoup(page.content, 'html.parser')
  items = soup.find_all('a', class_=className)
  filter_news(target, items)

def filter_news(target, items):
  print(target)
  for m in items:
    for n in keywords:
      check = [new['source'] for new in news]
      if ( n in m.text.strip().lower() or n in m['href'] ) and m['href'] not in check:
        news.append({
          "date": target.strftime('%Y-%m-%d'),
          "title": m.text.strip(),
          "text": "",
          "source": m['href'] 
        })
        continue

def main():
  init = date(2020, 1, 10)
  rollout(init)
  with open('data/cnbc.json', 'w') as f:
    json.dump(news, f)

if __name__ == "__main__":
  main()