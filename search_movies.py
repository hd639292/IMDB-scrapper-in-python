import requests
from bs4 import BeautifulSoup

class ImdbSearch(object):
	"""docstring for ImdbSearch"""
	def search_content(self , name):
		self.data = requests.get("https://www.imdb.com/find?q={}&s=tt&ttype=ft&ref_=fn_ft".format(name)).content
		self.soup = BeautifulSoup(self.data , 'html.parser')
		self.soup = self.soup.find('table')
		for self.tb in self.soup.find_all('tr'):
		    self.tb = self.tb.find_all('td')[1]
		    print(self.tb.find('a').text)
		    print("https://www.imdb.com/"+self.tb.find('a')['href'])

search = ImdbSearch()

name = input("ENTER THE MOVIE NAME: ")

search.search_content(name)





	
