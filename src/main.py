import tmdbsimple as tmdb
tmdb.API_KEY = 'your-api-key'

search = tmdb.Search()
response = search.movie(query='fast', page='2')
print (search.total_results)
print (search.page)
for s in search.results:
	print(s['title'], s['release_date'])
