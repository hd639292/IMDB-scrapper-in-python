from bs4 import BeautifulSoup
import requests
import pandas as pd

data = requests.get("https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating").content
soup = BeautifulSoup(data , 'html.parser')
soup = soup.find_all(class_ = "lister-item mode-advanced")
title = []
discription = []
votes = []
gross = []
pd_data = {
    'Title':title,
    'Discription':discription,
    'Votes':votes,
    'Gross':gross
}

for t in soup:
    #title scrapping
    title.append(str(t.find(class_ = "lister-item-header").text).replace("\n" , ""))
    
    #description
    discription.append(str(t.find_all('p')[1].text).strip())
    
    t = t.find(class_ = "sort-num_votes-visible")
   	#votes
    votes.append(t.find_all('span')[1].text)
    
    #gross
    gross.append(t.find_all('span')[-1].text)



df = pd.DataFrame(pd_data)
print(df)
