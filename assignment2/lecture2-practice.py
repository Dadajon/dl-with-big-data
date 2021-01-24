import urllib.request
from bs4 import BeautifulSoup

# url = 'http://books.toscrape.com/'
# html_document_1 = urllib.request.urlopen(url) #Acces html file (html 접속)
# open_web = html_document_1.read() #Read through the html code (접속한 파일 코드 읽어봐라)

# soup = BeautifulSoup(open_web, 'html.parser')

# # print(soup.title) #bring title tag of html doc
# # print(soup.title.text) #brings content of title tag of html doc

# #get the title of specific book

# #default > div.container-fluid.page > div > div > div > section > div: nth-child(2) > ol > li: nth-child(1) > article > h3 > a
# #default > div.container-fluid.page > div > div > div > section > div:nth-child(2) > ol > li:nth-child(2) > article > h3 > a
# title_of_book = soup.select_one(
#     "div.container-fluid.page > div > div > div > section > div:nth-child(2) > ol > li:nth-child(2) > article > h3 > a").string

# #default > div.container-fluid.page > div > div > div > section > div:nth-child(2) > ol > li:nth-child(1) > article > div.product_price > p.price_color
# price_of_book = soup.select_one(
#     "#default > div.container-fluid.page > div > div > div > section > div:nth-child(2) > ol > li:nth-child(2) > article > div.product_price > p.price_color").string

# print("Book title", title_of_book)
# print(price_of_book)

# # title: price
# print(f"{title_of_book}: {price_of_book}")

# title_of_book = ["A", "B", "C"]
# price_of_book = ["20", "10", "30"]

# title_price = list(zip(title_of_book, price_of_book))
# print(title_price)

# Task 2
# url = 'http://books.toscrape.com/'
# html_doc = urllib.request.urlopen(url)  # Acces html file (html 접속)
# open_web = html_doc.read()  # Read through the html code (접속한 파일 코드 읽어봐라)


# soup = BeautifulSoup(open_web, 'html.parser')

# print(soup.title)  # bring title tag of html doc
# print(soup.title.text)  # brings content of title tag of html doc

#get the title of specific book
# title_of_book = [h3.text for h3 in soup.select("h3")]

# titles_of_books = [titles.text for titles in soup.select("h3")]

# h3 = soup.select("h3")
# titles_of_books = list()
# for titles in soup.select("h3"):
#     titles_of_books.append(titles.text)
# # print(titles_of_books)

# # prices
# prices_of_books = list()
# for prices in soup.select("p.price_color"):
#     prices_of_books.append(prices.text)
# print(prices_of_books)

# title_price = list(zip(titles_of_books, prices_of_books))
# print(title_price)


# Task 2
url = "http://quotes.toscrape.com"
html_doc = urllib.request.urlopen(url)
open_web = html_doc.read()

soup = BeautifulSoup(open_web, 'html.parser')

# print(soup.title)  # bring title tag of html doc
# print(soup.title.text)  # brings content of title tag of html doc

# getAuthors = [small.text.strip() for small in soup.find_all("small", {"class": "author"})]
# print(getAuthors)

# <small class="author">Text</small>
# soup.select("small", {"class": "author"})
get_author = list()
for author in soup.find_all("small", {"class": "author"}):
    get_author.append(author.text)
# print(get_author)

get_quote = list()
for quote in soup.find_all("span", {"class": "text"}):
    get_quote.append(quote.text)
# print(get_quote)

# for i in range(len(get_author)):
#     print(f"{get_author[i]}: {get_quote[i]}")

# quote = [span.text.strip() for span in soup.find_all("span", {"class": "text"})]

# test = zip(get_author, get_quote)
# author_quote = list(test)

author_quote = list(zip(get_author, get_quote))
print(author_quote[1])
