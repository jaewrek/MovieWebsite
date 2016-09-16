# Video class, parent to Movie class
# Constructor takes in Title and Duration of video object.
class Video():
	#def __doc__(self):
		#return "Video class, parent to movie and tv_show. Contains title and duration of video"
	def __init__(self, title, duration):
		self.title = title
		self.duration = duration

	def show_info(self):
		print("Title is - "+self.title)
		print("Duration is - "+self.duration)

	valid_ratings = ["G","PG","PG-13","R"]
		