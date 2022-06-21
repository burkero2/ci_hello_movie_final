from django.test import TestCase
from .models import Movie


# Create your tests here.
class TestViews(TestCase):

    def test_get_movie_list(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_app/movie_app_home.html')

    # Remove from Challenge (maybe)
    def test_movie_app_add_page(self):
        response = self.client.get("/add")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_app/movie_app_add.html')

    def test_movie_app_edit_page(self):
        movie = Movie.objects.create(
            title='Test Todo Item', 
            director='Test Movie Items', 
            genre='Test Movie Items', 
            description='', 
            rating=5, 
            watched=False, 
            imdb_link = 'https://www.imdb.com/title/tt0058331/?ref_=fn_al_tt_1')
        response = self.client.get(f'/edit/{movie.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_app/movie_app_edit.html')

    def test_can_add_movie(self):
        response = self.client.post('/add', 
            {
            "title": "Blade Runner",
            "director": "Ridley Scott",
            "genre": "Science Fiction",
            "description": "A blade runner must pursue and terminate four replicants who stole a ship in space, and have returned to Earth to find their creator.",
            "rating": 4,
            "watched": False,
            "imdb_link": "https://www.imdb.com/title/tt0083658/",
        })
        self.assertRedirects(response, '/')


    def test_can_delete_movie(self):
        movie = Movie.objects.create(
            title='Test Todo Item', 
            director='Test Movie Items', 
            genre='Test Movie Items', 
            description='', 
            rating=5, 
            watched=False, 
            imdb_link = 'https://www.imdb.com/title/tt0058331/?ref_=fn_al_tt_1')
        response = self.client.get(f'/delete/{movie.id}')
        self.assertRedirects(response, '/')
        existing_movie_list = Movie.objects.filter(id = movie.id)
        self.assertEqual(len(existing_movie_list), 0)

    def test_can_toggle_movie(self):
        movie = Movie.objects.create(
            title='Test Todo Item', 
            director='Test Movie Items', 
            genre='Test Movie Items', 
            description='', 
            rating=5, 
            watched=True, 
            imdb_link = 'https://www.imdb.com/title/tt0058331/?ref_=fn_al_tt_1')
        response = self.client.get(f'/toggle/{movie.id}')
        self.assertRedirects(response, '/')
        updated_movie = Movie.objects.get(id=movie.id)
        self.assertFalse(updated_movie.watched)

    # Remove from Challenge (this comes in the Coverage video)
    def test_can_edit_movie(self):
        movie = Movie.objects.create(
            title= "Blade Runner",
            director= "Ridley Scott",
            genre= "Science Fiction",
            description= "A blade runner must pursue and terminate four replicants who stole a ship in space, and have returned to Earth to find their creator.",
            rating= 4,
            watched= False,
            imdb_link= "https://www.imdb.com/title/tt0083658/",)
        response = self.client.post(f'/edit/{movie.id}', 
            {
            "title": "Blade Runner",
            "director": "Ridley Scott",
            "genre": "Science Fiction",
            "description": "A blade runner must pursue and terminate four replicants who stole a ship in space, and have returned to Earth to find their creator.",
            "rating": 5,
            "watched": False,
            "imdb_link": "https://www.imdb.com/title/tt0083658/",
        })
        self.assertRedirects(response, '/')
        updated_movie = Movie.objects.get(id=movie.id)
        self.assertEquals(updated_movie.rating, 5)
