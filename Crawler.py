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

        # finding all the h2, h3 and p tags
        links = soup.find_all(["h2", "h3", "p"])
        pageName = soup.find("h1")

        #creating a .txt file to save the info
        with open (pageName.text + '.txt', 'w', encoding = "utf-8") as fp: 

            #going through each tag and writing the info on the .txt file
            for link in links:
                fp.write(link.text)

            print("File created succesfully!\n")

        #loop which runs until the user enters a correct input
        while True:
                userInput = input("Would you like to open the current text file? (Enter Yes or No): ")

                if userInput == "Yes":
                   with open(pageName.text + '.txt', 'r') as textFile:
                        print("\nText file begins:\n")
                        print(textFile.read())
                        break

                elif userInput == "No":
                   print("Exiting program...")
                   break

                else: 
                    print("Incorrect input. Try again.")

    else: 

        print("Incorrect URL! Enter a correct URL.")

print("Hi! Welcome to Araneae!")
print("This is a spiderbot that browses the user specified Wikipedia page and stores all the text of the page in a .txt file\n")
wikiCrawler() #calling the crawler function