import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
    "Accept-Language":"en,en-US;q=0.9,sv;q=0.8"
}


url = "https://www.amazon.com/UGREEN-Coupler-Ethernet-Extender-Connector/dp/B016B13U9Y/ref=sr_1_3?crid=1KU8LQFN71VHU&keywords=ethernet+extender&qid=1648573618&sprefix=%2Caps%2C145&sr=8-3"


request = requests.get(url=url, headers=headers).text

soup = BeautifulSoup(request, "html.parser")

price = float(soup.find_all(class_="a-offscreen")[0].text.strip("$"))