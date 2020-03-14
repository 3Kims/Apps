##########!!!!!!! ERROR ON 28TH LINE FOR INVALID INDEX ==== NO INPUT FROM SORUCE


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://store.musinsa.com/app/contents/bestranking/'

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
infos = page_soup.findAll("div",{"class":"article_info"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, name, price, like\n"

f.write(headers)

for info in infos:
####브랜드
##brand = info.findAll("div",{"class":"article_info"})
	brand = info.p.a.text

####가격
	info_price = info.findAll("span",{"class":"txt_price_member"})
	price = info_price[0].text

###이름
	info_name = info.findAll("p",{"class":"list_info"})
	name = info_name[0].a["title"]

###좋아요 수
	info_like = info.findAll("p",{"class":"txt_cnt_like"})
	like = info_like[0].text.strip()

	print("brand: " + brand)
	print("name: " + name)
	print("price: " + price)
	print("like: " + like)

	f.write(brand + "," + name + "," + price.replace(",","") + "," + like.replace(",","") + "\n")

f.close()

