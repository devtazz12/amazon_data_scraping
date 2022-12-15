import pandas as pd
import requests
from bs4 import BeautifulSoup


headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
        'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'
    }


data=[]

url_list=[
'https://www.amazon.com/s?i=electronics&srs=17938598011&bbn=17938598011&dc&qid=1670407309&ref=sr_pg_1',
'https://www.amazon.com/s?i=electronics&srs=17938598011&bbn=17938598011&dc&page=2&qid=1670407319&ref=sr_pg_2',
'https://www.amazon.com/s?i=electronics&srs=17938598011&bbn=17938598011&dc&page=3&qid=1670407358&ref=sr_pg_3',
'https://www.amazon.com/s?i=electronics&srs=17938598011&bbn=17938598011&dc&page=4&qid=1670407381&ref=sr_pg_4',
'https://www.amazon.com/s?i=electronics&srs=17938598011&bbn=17938598011&dc&page=5&qid=1670407408&ref=sr_pg_5',
'https://www.amazon.com/s?i=electronics&srs=17938598011&bbn=17938598011&dc&page=6&qid=1670407433&ref=sr_pg_6',
'https://www.amazon.com/s?i=electronics&srs=17938598011&bbn=17938598011&dc&page=7&qid=1670407476&ref=sr_pg_7',
'https://www.amazon.com/s?i=electronics&srs=17938598011&bbn=17938598011&dc&page=8&qid=1670407500&ref=sr_pg_8',
'https://www.amazon.com/s?i=electronics&srs=17938598011&bbn=17938598011&dc&page=9&qid=1670407525&ref=sr_pg_9',
'https://www.amazon.com/s?i=electronics&srs=17938598011&bbn=17938598011&dc&page=10&qid=1670407546&ref=sr_pg_10',
'https://www.amazon.com/s?i=electronics&srs=17938598011&bbn=17938598011&dc&page=11&qid=1670407570&ref=sr_pg_11',
'https://www.amazon.com/s?i=electronics&srs=17938598011&bbn=17938598011&dc&page=12&qid=1670407590&ref=sr_pg_12',
'https://www.amazon.com/s?i=electronics&srs=17938598011&bbn=17938598011&dc&page=13&qid=1670407611&ref=sr_pg_13',
'https://www.amazon.com/s?k=men+fashion&qid=1670411828&sprefix=%2Caps%2C398&ref=sr_pg_1',
'https://www.amazon.com/s?k=men+fashion&page=2&qid=1670411856&sprefix=%2Caps%2C398&ref=sr_pg_2',
'https://www.amazon.com/s?k=men+fashion&page=3&qid=1670412912&sprefix=%2Caps%2C398&ref=sr_pg_3',
'https://www.amazon.com/s?k=men+fashion&page=4&qid=1670412934&sprefix=%2Caps%2C398&ref=sr_pg_4',
'https://www.amazon.com/s?k=men+fashion&page=5&qid=1670412960&sprefix=%2Caps%2C398&ref=sr_pg_5',
'https://www.amazon.com/s?k=men+fashion&page=6&qid=1670412993&sprefix=%2Caps%2C398&ref=sr_pg_6',
'https://www.amazon.com/s?k=men+fashion&page=7&qid=1670413046&sprefix=%2Caps%2C398&ref=sr_pg_7',
'https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A7141123011%2Cn%3A16225020011%2Cn%3A1040664&qid=1670913186&ref=sr_pg_1',
'https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A7141123011%2Cn%3A16225020011%2Cn%3A1040664&page=2&qid=1670913195&ref=sr_pg_2',
'https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A7141123011%2Cn%3A16225020011%2Cn%3A1040664&page=3&qid=1670913232&ref=sr_pg_3',
'https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A7141123011%2Cn%3A16225020011%2Cn%3A1040664&page=4&qid=1670913262&ref=sr_pg_4',
'https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A7141123011%2Cn%3A16225020011%2Cn%3A1040664&page=5&qid=1670913284&ref=sr_pg_5',
'https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A7141123011%2Cn%3A16225020011%2Cn%3A1040664&page=6&qid=1670913321&ref=sr_pg_6',
'https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A7141123011%2Cn%3A16225021011%2Cn%3A1040666&qid=1670913854&ref=sr_pg_1',
'https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A7141123011%2Cn%3A16225021011%2Cn%3A1040666&page=2&qid=1670913862&ref=sr_pg_2',
'https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A7141123011%2Cn%3A16225021011%2Cn%3A1040666&page=3&qid=1670913890&ref=sr_pg_3',
'https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A7141123011%2Cn%3A16225021011%2Cn%3A1040666&page=4&qid=1670913936&ref=sr_pg_4',
'https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A7141123011%2Cn%3A16225021011%2Cn%3A1040666&page=5&qid=1670913957&ref=sr_pg_5',
'https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A7141123011%2Cn%3A16225021011%2Cn%3A1040666&page=6&qid=1670913982&ref=sr_pg_6',
'https://www.amazon.com/s?i=fashion-boys-intl-ship&bbn=16225021011&rh=n%3A7141123011%2Cn%3A16225021011%2Cn%3A1040666&page=7&qid=1670914002&ref=sr_pg_7',
'https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A1040660&qid=1670914083&ref=sr_pg_1',
'https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A1040660&page=2&qid=1670914090&ref=sr_pg_2',
'https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A1040660&page=3&qid=1670914109&ref=sr_pg_3',
'https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A1040660&page=4&qid=1670914087&ref=sr_pg_4',
'https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A1040660&page=5&qid=1670914156&ref=sr_pg_5',
'https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A1040660&page=6&qid=1670914180&ref=sr_pg_6',
'https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A1040660&page=7&qid=1670914203&ref=sr_pg_7'

]

for j in url_list:
    url=f"{j}"
 
    r= requests.get(url, headers=headers)
    soup= BeautifulSoup(r.text, 'html.parser')
    titles = soup.findAll('span', {'class':'a-size-small a-color-base a-text-normal'})
    ratings = soup.findAll('span', {'class':'a-icon-alt'})
    img_urls=soup.find_all('img',{'class':'s-image'})
    title_list=[]
    rating_list=[]
    imgurl_list=[]

    # appending into list 
    for img_url in img_urls:
        if 'jpg' in img_url['src']:
            imgurl_list.append(img_url['src'])

    for title in titles:
        title_list.append(title.text)
    for rating in ratings:
        rating_list.append(rating.text.replace(' out of 5 stars',''))


    # inserting list into list name data
    for i in range(0,13):
        
        obj1=title_list[i]
        obj2=rating_list[i]
        obj3=imgurl_list[i]
        data.insert(i, [obj1,obj2,obj3])



df = pd.DataFrame(data, columns=['title','ratings','img_url'])
df.to_csv('recm.csv')
