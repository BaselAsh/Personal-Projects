
"""
This program is for web scraping using requests module and beautifulsoup module 
The development of the app started in 9/8/2023 by Basel Ashraf
"""
# TODO Use modules to parse the javascript code in here not using any website that parses that code

# import requests
# from bs4 import BeautifulSoup
# from selectolax.parser import HTMLParser
# import pyjsparser
import modtest


def main():
    """ This Is The Main Function """
    # url = "https://metwallylabs.com/backendroadmap.html"
    # response = requests.get(url)
    # html = response.text
    # soup = BeautifulSoup(html, "lxml")
    # subjects = soup.find_all("script")[3]
    # names = subjects.text
    # print(pyjsparser.parse(names))
    names = modtest.names
    for n in names:
        print("-=====-=====-=====-")
        print(f"Main -> {n['name']}")
        print("Sub: ")
        for i in n["sub"]:
            print(f"  -{i}")


if __name__ == "__main__":
    main()
