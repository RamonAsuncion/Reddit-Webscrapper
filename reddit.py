from bs4 import BeautifulSoup
import requests
from time import sleep


# test link https://www.reddit.com/r/ProgrammerHumor/comments/j0uoo1/the_struggle_gets_real_when_the_family_gets/

# Sort by: Best, Top, New, Controversial, Old, Q&A and grabs the first top element (first top comment)


def ask_for_link():
    url = input('Please input the url: ')
    print(url)
    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'lxml')


def main():
    ask_for_link()


if __name__ == '__main__':
    main()
