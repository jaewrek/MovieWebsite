from video import Video

# Movie class, child to Video class
# Constructor takes in Title, Duration, Storyline, Image, Trailer, Actors, and Year of movie object as
# arguments.
class Movie(Video):
	def __init__(self, title, duration, movie_storyline, poster_image, trailer_youtube, actors, year):
		Video.__init__(self, title, duration)
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.actors = actors
		self.release_date = year

		self.valid_ratings = ["G","PG","PG-13","R"]
		
