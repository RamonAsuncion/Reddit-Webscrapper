from bs4 import BeautifulSoup
import requests
from time import sleep
import urllib.request


# Need Regex to check if valid link and request 200 to check if link is working
def ask_for_link():
    url = input('Please input the url: ')
    print("Debug: {}".format(url))

    check_response = requests.get(url)

    # For testing check for page request will be probably implemented
    if check_response.status_code == 200:
        print("Reached!")
    else:
        print("Failed")

    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'lxml')


def main():
    ask_for_link()


if __name__ == '__main__':
    main()
