# Jerrik Neri
# Intro to Programming ND
# Project 4
# Udacity

# Creating movie objects using the Movie class to pass in fresh_tomatoes to generate HTML.

from media import Movie
import fresh_tomatoes2


# instantiating all movie objects with appropriate information/arguments
rush_hour = Movie("Rush Hour",
						"98",
						"An LAPD officer and Hong Kong Detective come together to bring down a Chinese Druglord.",
						"http://resizing.flixster.com/ep6MeG-pa6yqG4fr50-UKURFD9Q=/800x1200/v1.bTsxMTE2OTc2NDtqOzE3MTM4OzIwNDg7ODAwOzEyMDA",
						"https://www.youtube.com/watch?v=JMiFsFQcFLE",
						"Jackie Chan & Chris Tucker",
						"1998")
rush_hour.valid_ratings = "PG-13"

warcraft = Movie("Warcraft",
					   "123",
					   "A tale of two races from two separate worlds clashing together for survival.",
					   "http://www.korsgaardscommentary.com/wp-content/uploads/2016/07/warcraft-movie-poster.jpg",
					   "https://www.youtube.com/watch?v=RhFMIRuHAL41",
					   "Toby Kebbel & Daniel Wu",
					   "2016")
warcraft.valid_ratings = "PG-13"

shutter_island = Movie("Shutter Island",
							 "138",
							 "A rookie CIA detective is sent to Shutter Island to investigate a missing pateint.",
							 "http://66.media.tumblr.com/tumblr_m8itmy8AOF1raij5vo1_1280.jpg",
							 "https://www.youtube.com/watch?v=5iaYLCiq5RM",
							 "Leonardo DiCaprio",
							 "2010")
shutter_island.valid_ratings = "R"

good_will_hunting = Movie("Good Will Hunting",
								"126",
								"A young misguided youth with genius-level IQ battle the problems of his past while trying to move forward into his new life of opportunity.",
								"http://cdn.miramax.com/media/assets/726_GoodWillHunting_Catalog_Poster-BB_v2_Approved.png",
								"https://www.youtube.com/watch?v=PaZVjZEFkRs",
								"Matt Damon, Ben Affleck, & Robin Williams",
								"1997")
good_will_hunting.valid_ratings = "R"

the_debut = Movie("The Debut",
				  "94",
				  "A high school Filipino-American teen struggles with the cultural clash between his family and fitting in with his friends.",
				  "https://upload.wikimedia.org/wikipedia/en/thumb/5/5a/DebutDVDcoverfinal.jpg/220px-DebutDVDcoverfinal.jpg",
				  "https://www.youtube.com/watch?v=6htYeILov58",
				  "Dante Basco, Joy Bisco, & Eddie Garcia",
				  "2001")
the_debut.valid_ratings = "R"

eternal_sunshine = Movie("Eternal Sunshine of the Spotless Mind",
						 "108",
						 "After a sudden break up a man attempts to erase his mind.",
						 "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
						 "https://www.youtube.com/watch?v=quuMv7cGUn0",
						 "Jim Carey",
						 "2004")
eternal_sunshine.valid_ratings = "R"

# list of movies to be passed into fresh_tomatoes2 to generate HTML
movies = [rush_hour, warcraft, shutter_island, good_will_hunting, the_debut, eternal_sunshine]
fresh_tomatoes2.open_movies_page(movies)
