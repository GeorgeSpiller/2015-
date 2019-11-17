from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.youtube.com/"

#opening up connection, grabbing the page with urllib.request
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")
#grabs each recomended video
containers = page_soup.findAll("div",{"id":"dismissable"})
