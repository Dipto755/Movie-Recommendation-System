import json
from KNN_Algo import KNearestNeighbours




with open('movie_data.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
with open('movie_title2.json', 'r+', encoding='utf-8') as f:
    movie_titles = json.load(f)


def KNN_Movie_Recommender(test_point, k):
    
    target = [0 for item in movie_titles]
   
    model = KNearestNeighbours(data, target, test_point, k=k)
    
    model.fit()
    
    table = []
    for i in model.indices:

        table.append([movie_titles[i][1], movie_titles[i][4],data[i][-1]])
    print(table)
    return table

