import requests
import operator
from bs4 import BeautifulSoup

class SortedMovie(object):
	__slots__ = ['movie_title' , 'votes' , 'ratings']
	def __init__(self , movie_title , votes , ratings):
		self.movie_title = movie_title
		self.votes = votes
		self.ratings = ratings

movies_obj = []
links = []

n = int(input("NUMBER OF MOVIES YOU WANT TO COMPARE: "))
for i in range(n):
	links.append(input('Enter the link of {}st: '.format(i+1)))

def get_rating(links):
    data = requests.get(str(links)).text
    soup = BeautifulSoup(data , 'html.parser')
    try:
    	title = soup.find(class_ = "title_wrapper")('h1')[0].text
    	vote = soup.find(class_ = "ratings_wrapper")('span')[0].text
    	rating = soup.find(class_ = "ratings_wrapper")('span')[3].text
    	return title , vote , rating
    except Exception:
    	title = soup.find(class_ = "title_wrapper")('h1')[0].text
    	vote = 0
    	rating = "This Movie might be in devolopment"
    	return title , vote , rating
    

for link in links:
    res = get_rating(link)
    movies_obj.append(SortedMovie(res[0] , res[1], res[2]))

sort_movies_obj = sorted(movies_obj , key= operator.attrgetter('votes') , reverse= True)

for mov in sort_movies_obj:
    print("Title: {}".format(mov.movie_title)) 
    print("Votes: {}".format(mov.votes))
    print("Total votes: {} \n ______________ \n".format(mov.ratings))