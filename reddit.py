from bs4 import BeautifulSoup
import requests
# test link https://www.reddit.com/r/ProgrammerHumor/comments/j0uoo1/the_struggle_gets_real_when_the_family_gets/

url = input('Please input the url: ')
source = requests.get(url)
soup = BeautifulSoup(source.content, 'lxml')

print(url)


def main():
    return


if __name__ == 'main':
    main()
