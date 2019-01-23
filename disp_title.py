import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue').read()

soup = bs.BeautifulSoup(source,'lxml')

print(soup.title.string)


