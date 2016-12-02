import tmdbsimple as tmdb
import ConfigParser
import time
import os
from datetime import datetime

config = ConfigParser.RawConfigParser()
config.read('movlibgen.cfg')
x = 'abcdefghijklmnopqrstuvwxyz'
path = config.get('CONFIG', 'PATH')
samplefile = config.get('CONFIG', 'SAMPLE')
tmdb.API_KEY = config.get('CONFIG', 'API_KEY')
search = tmdb.Search()

for i in x:
	for p in range(1, 20):
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
				fakemovie += ".mp4"

				fullsample = path
				fullsample += "/"
				fullsample += samplefile

				fullfakemovie = path
				fullfakemovie += "/"
				fullfakemovie += fakemovie

				print(str(s['title']), movie_year)
				os.symlink(fullsample, fullfakemovie)
			except:
				print "Skip to next"
		time.sleep(1)
