import bs4 as bs
import urllib.request



source = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue').read()
soup = bs.BeautifulSoup(source,'lxml')

table=soup.table
#print(table)


table_rows=table.find_all('tr')

for tr in table_rows:
    td =tr.find_all('td')
    row=[i.string for i in td]
    print(row)
