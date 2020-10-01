from bs4 import BeautifulSoup
import requests
# test link https://www.reddit.com/r/ProgrammerHumor/comments/j0uoo1/the_struggle_gets_real_when_the_family_gets/

# Sort by: Best, Top, New, Controversial, Old, Q&A and grabs the first top element (first top comment)

url = input('Please input the url: ')
source = requests.get(url)
soup = BeautifulSoup(source.content, 'lxml')

print(url)


def main():
    data_collected_from = []
    return


if __name__ == 'main':
    main()
