import requests_with_caching
import json

def get_movies_from_tastedive(title):
    baseurl = 'https://tastedive.com/api/similar'
    param = {}
    param['q'] = title
    param['limit'] = 5
    param['type'] = 'movies'
    
    res = requests_with_caching.get(baseurl, params=param)
    return json.loads(res.text)
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
def extract_movie_titles(dic):
    titles=[]
    for i in dic['Similar']['Results']:
        titles.append(i['Name'])
    return titles
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
def get_related_titles(movie_list):
    li = []
    for movie in movie_list:
        li.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(li))
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
def get_movie_data(title):
    baseurl = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    
    res = requests_with_caching.get(baseurl, params=param)
    return json.loads(res.text)

def get_movie_rating(dictionary):
    dic=dictionary['Ratings']
    for item in dic:
        if item['Source']=='Rotten Tomatoes':
            return int(item['Value'][:-1])
    return 0
def get_sorted_recommendations(movie_list):
    t_r = {}
    for title in get_related_titles(movie_list):
        t_r[title] = get_movie_rating(get_movie_data(title))
    return [i[0] for i in sorted(t_r.items(), key=lambda item: (item[1], item[0]), reverse=True)]
get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
