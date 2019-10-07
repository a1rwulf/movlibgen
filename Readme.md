# movlibgen
Pythonscript that will query themoviedb.org for movie titles.
You can specify one working videofile and the script will generate symlinks to that file
with the names scraped from tmdb.
Then you can point your kodi instance to your fakemovies and let it build a movie database.
With this script it is very easy to build libraries of thousands of movies for development.

## configuration
Create a config file movlibgen.cfg besides the pyhthon script.
Here is a sample contents:
```
[CONFIG]
API_KEY = 03e61ca1b9fdffcfdb40c1f7d6c5fh27
PATH = /home/youruser/Videos/fakelibrary
SAMPLE = test.ts
```
