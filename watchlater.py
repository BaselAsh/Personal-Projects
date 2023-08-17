"""
- This app is for opening YouTube watch later
- This app was created in 19/6/2023 by Basel Ashraf
- This app was finished in 19/6/2023
"""

from selenium import webdriver


def main():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/playlist?list=PLCjzkNC2bIsef1F34BK7_kp7ldAObcC4G")
    input("Press enter to quit the window")
    driver.quit()


if __name__ == "__main__":
    main()
