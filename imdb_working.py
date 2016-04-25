# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 23:22:20 2016

@author: Prateek
"""

import requests
from bs4 import BeautifulSoup

print ('Enter movie/Tv series name')
movie = input()
print ()
url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q='+movie+'&s=all'

source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'lxml')

for td in soup.findAll('td',{'class':'result_text'}):
    href = td.find('a')['href']
    movie_page = 'http://www.imdb.com'+href
    break

def get_title(movie_url):
    source_code = requests.get(movie_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'lxml')
    for title in soup.findAll('div',{'class':'title_wrapper'}):
        return title.find('h1').text.rstrip()

movie_name = get_title(movie_page)

def get_movie_data(movie_url):
    source_code = requests.get(movie_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'lxml')
    for div in soup.findAll('div',{'class':'ratingValue'}):
        print ('Imdb rating of the movie/Tv Series "'+movie_name+'" is: ',end='')
        print (div.text)
        print ()

    for div in soup.findAll('div',{'class':'summary_text'}):
        print ('Summary of the movie/Tv series:')
        print (div.text.lstrip())

get_movie_data(movie_page)

'''print_genre = soup.findAll('div',{'class':'subtext'})
for div in print_genre:
    for genre in print_genre.findAll('a'):
        print (genre.text,end=' |')
        print ()'''
