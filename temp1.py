import requests
from bs4 import BeautifulSoup

thing = input("Enter the thing : ")
url = 'https://www.google.com/search?tbm=isch&q='+thing
r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content,'lxml')
print(soup.a)
