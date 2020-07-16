import requests
from bs4 import BeautifulSoup

url = input("Enter the URL: ")

result = requests.get(url)

if result.status_code == 200:
    print(result)

else: 
    print("Incorrect URL!")


