"""
This program is for learning web scraping
Basel Ashraf made this in 10/6/2023
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def main():
    """ This is the main function """
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")
    search_bar = driver.find_element("search_query", by=By.NAME)
    search_bar.send_keys("Python programming")
    search_bar.send_keys(Keys.RETURN)
    input("Press enter to close the window")
    driver.quit()



if __name__ == "__main__":
    main()
