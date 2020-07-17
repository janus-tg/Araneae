import requests
from bs4 import BeautifulSoup

#wikipedia info crawler

def wikiCrawler():

    #getting the url from the user
    url = input("Enter the Wikipedia URL: ")
    result = requests.get(url)

    #if else codeblock if the code is succesful

    if result.status_code == 200:
        src = result.content
        soup = BeautifulSoup(src, "lxml")
        links = soup.find_all(["h2", "h3", "p"])
        for link in links:
             print(link.text)
    else: 
        print("Incorrect URL! Enter a correct URL.")

   