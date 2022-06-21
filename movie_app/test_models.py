from django.test import TestCase
from .models import Movie

# Create your tests here.

class TestModels(TestCase):
    def test_watched_defaults_to_false(self):
        movie = Movie.objects.create(
            title= "Blade Runner",
            director= "Ridley Scott",
            genre= "Science Fiction",
            description= "A blade runner must pursue and terminate four replicants who stole a ship in space, and have returned to Earth to find their creator.",
            rating= 4,
            imdb_link= "https://www.imdb.com/title/tt0083658/",)
        self.assertFalse(movie.watched)
    
    def test_movie_string_method_returns_title(self):
        movie = Movie.objects.create(
            title= "Blade Runner",
            director= "Ridley Scott",
            genre= "Science Fiction",
            description= "A blade runner must pursue and terminate four replicants who stole a ship in space, and have returned to Earth to find their creator.",
            rating= 4,
            imdb_link= "https://www.imdb.com/title/tt0083658/",)
        self.assertEqual(str(movie), "Blade Runner")