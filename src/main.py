import tmdbsimple as tmdb
import configparser
import time
import os
from datetime import datetime

config = configparser.ConfigParser()
config.read('movlibgen.cfg')
x = 'abcdefghijklmnopqrstuvwxyz'
path = config.get('CONFIG', 'PATH')
samplefile = config.get('CONFIG', 'SAMPLE')
tmdb.API_KEY = config.get('CONFIG', 'API_KEY')
search = tmdb.Search()

for i in x:
	for p in range(1, 400):
		response = search.movie(query=i, page=str(p), include_adult='no')
		print (search.total_results)
		print (search.page)
		for s in search.results:
			try:
				movie_year = ''
				if s['release_date'] != '':
					dt = datetime.strptime(s['release_date'], '%Y-%m-%d')
					movie_year = dt.year
				fakemovie = str(s['title'])
				fakemovie = fakemovie.replace(" ", "_")
				fakemovie += "_"
				fakemovie += str(movie_year)
				fakemovie += ".ts"

				fullsample = path
				fullsample += "/"
				fullsample += samplefile

				fullfakemovie = path
				fullfakemovie += "/"
				fullfakemovie += fakemovie

				print(str(s['title']), movie_year)
				os.symlink(fullsample, fullfakemovie)
			except Exception as e:
				print ("Skip to next" + str(e))
		time.sleep(1)
