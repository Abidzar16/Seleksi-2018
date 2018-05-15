import parsingweb
from parsingweb import soup #mengambil variabel soup

# list untuk menyimpan data
titles = []
prices = []
sellers = []
ranks = []

#mengambil semua
title = soup.find_all('a',class_ ='product__name line-clamp--2 js-tracker-product-link')
price = soup.find_all('span', class_ = 'amount positive')
name = soup.find_all('h5', class_ = 'user__name')
rank = soup.find_all('div', class_ = 'user-feedback-container clearfix')
#meskipun ada 50 data dalam satu page, yang diambil hanya 40 saja

for x in range(0, 40):
    
    titles.append(title[x].text)
    
    draft = price[x].text
    newprice = int(draft.replace('.',''))
    prices.append(newprice)
    
    nama = name[x].a.text
    sellers.append(nama)
    
    ranking = rank[x].div.span.text
    ranks.append(ranking)

