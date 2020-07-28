import requests

from bs4 import BeautifulSoup

from concurrent.futures import ThreadPoolExecutor

import time

urls = ["https://www.imdb.com//title/tt2980516/" ,
"https://www.imdb.com//title/tt0787524/",
"https://www.imdb.com//title/tt1285016/",
"https://www.imdb.com//title/tt0268978/"
]
movie_data = []

result = []

def get_rating(session , url):
	with session.get(url) as response:
		movie_data.append(response.text)

def request_executor(executor , func , session):
	with executor as ex:
		ex.map(func , [session]*len(urls) , urls)

		ex.shutdown(wait=True)


executor = ThreadPoolExecutor(max_workers= 55)
session = requests.Session()

t1 = time.perf_counter()

request_executor(executor, get_rating , session)


for data in movie_data:
	soup = BeautifulSoup(data , 'html.parser')
	title = str(soup.find(class_ = "title_wrapper")('h1')[0].text)
	title = title.replace("\xa0", " ")
	rating = soup.find(class_ = "ratings_wrapper")('span')[0].text
	vote = soup.find(class_ = "ratings_wrapper")('span')[3].text
	result.append((title , float(rating) , vote))


new_result = sorted(result , key = lambda x : x[1] , reverse= True)

for res in new_result:
	print(res)

t2 = time.perf_counter()


print(f"Taken time : {t2-t1}")
