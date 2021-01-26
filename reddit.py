from bs4 import BeautifulSoup
import requests
from time import sleep
import urllib.request
from urllib.parse import urlparse


# Need Regex to check if valid link and request 200 to check if link is working
def ask_for_link():
    url = input('Please input the url: ')

    if not urlparse(url).scheme:
        url = 'https://' + url

    print("Debug: {}".format(url))

    # Request
    check_response = urllib.request.urlopen(url).getcode()

    if check_response == 200:
        print('Debug: Reached!')
    else:
        print('Debug: Failed')

    # For testing check for page request will be probably implemented
    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'lxml')


def main():
    ask_for_link()


if __name__ == '__main__':
    main()
