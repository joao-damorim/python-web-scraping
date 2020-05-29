import requests
from bs4 import BeautifulSoup

#res = requests.get("https://digitalinnovation.one/blog/")
#res.encoding = "utf-8"

res = requests.get("https://tecnoblog.net/")
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')

posts = soup.find_all(class_="bloco")

all_posts = []
for post in posts:
    print(post.find('h2').text)

print(all_posts)