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
    info = post.find(class_= "texts")
    info2 = post.find(class_= "info")
    info3 = post.find(class_ = "entry")
    titulo = info.h2.text
    autor = info2.a.text
    noticia = info3.p.text

    print(autor)

print(all_posts)