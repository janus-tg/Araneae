import requests
from bs4 import BeautifulSoup
import os

#wikipedia info crawler

def wikiCrawler():

    #getting the url from the user
    url = input("Enter the Wikipedia URL: ")
    result = requests.get(url)

    #if else codeblock if the code is succesful

    if result.status_code == 200:

        src = result.content
        soup = BeautifulSoup(src, "lxml")

        # finding all the h2, h3 and p tags
        links = soup.find_all(["h2", "h3", "p"])
        pageName = soup.find("h1")

        #creating a .txt file to save the info
        with open (pageName.text + '.txt', 'w', encoding = "utf-8") as fp: 

            #going through each tag and writing the info on the .txt file
            for link in links:
                fp.write(link.text)

        while True:
                us = input("Would you like to open the current text file? (Enter Yes or No): ")

                if us == "Yes":
                   with open(pageName.text + '.txt', 'r') as file:
                        print("\n\n")
                        print(file.read())
                        break

                elif us == "No":
                   print("File was created succesfully. Exiting program...")
                   break

                else: 
                    print("Incorrect input. Try again.")

    else: 

        print("Incorrect URL! Enter a correct URL.")

print("Hi! Welcome to Aranae!\n This is a spiderbot which crawls a given Wikipedia URL and stores the information in a")
print(".txt file and stores all the references for the Wikipedia article in a .csv file\n")
wikiCrawler()