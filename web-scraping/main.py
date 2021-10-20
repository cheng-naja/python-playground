from bs4 import BeautifulSoup
import requests
import csv

title_list = []
degree_list = []

try:
  for i in range(1):
    i += 1
    url = 'https://www.bachelorstudies.com/Bachelor/USA/?page=' + str(i) 
    res = requests.get(url)
    res.encoding = "utf-8"

    if res.status_code == 200:
      print("success" + str(i))
      soup = BeautifulSoup(res.text, 'html.parser')
      all_title = soup.find_all("div", {"class": "program_title"})
      all_degree = soup.find_all("div", {"class": "degree"})

      index = 0
      for x in all_title:
        title = x.a.text
        if title not in title_list:
          title_list.append(str(x.a.text))
          degree_list.append(str(all_degree[index].select_one(".label-item").text.strip()))
        index += 1
    else:
      print('end at ' + str(i))
      break
except:
  print('end game')

fieldnames = ['title_list', 'degree_list']
f = open('web-scraping/data/test.csv', 'w', encoding='UTF8')
with f:
  writer = csv.DictWriter(f, fieldnames=fieldnames)
  writer.writeheader()
  index = 0
  for row in title_list:
    writer.writerow({'title_list': title_list[index], 'degree_list': degree_list[index]})
    index += 1
