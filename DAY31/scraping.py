
from bs4 import BeautifulSoup
import html5lib
import requests

# user input of url
# url = input("Enter the url : ")

# url = "https://www.codewithharry.com"
url = "https://en.wikipedia.org/wiki/Subhas_Chandra_Bose"

# getting the html from the given url

r = requests.get(url) # getting the url
content = r.content   # getting the html content
print(content)

# Parsing the HTML content
soup = BeautifulSoup(content,'html.parser')  # getting the raw html
print(soup)
print(soup.beautify)  # beautifies the html parsed
print(soup.prettify)  # beautifies the html parsed

# traversing the html content
title = soup.title # getting the title
print(title)
print(type(title))

head = soup.head  # targetting elements by tagname
print(head)

paragraphs = soup.p
print(paragraphs)


# targetting elements by tagname
paras = soup.find_all('p')
print(paras)
print(soup.find('sup')['class'])  # returns the class of the first paragraph
anc = soup.find_all('a')
for a in anc:
    # print(a)
    print(a.get('href'))


# getting the text from elements

print(soup.find('p').get_text)

