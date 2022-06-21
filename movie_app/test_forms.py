from django.test import TestCase
from .forms import MovieForm


# Create your tests here.
class TestDjango(TestCase):

    def test_movie_title_is_required(self):
        form = MovieForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_description_field_is_not_required(self):
        form = MovieForm({
            "title": "Blade Runner",
            "director": "Ridley Scott",
            "genre": "Science Fiction",
            "rating": 4,
            "watched": False,
            "imdb_link": "https://www.imdb.com/title/tt0083658/",
        })
        self.assertTrue(form.is_valid())

    def test_watched_field_is_not_required(self):
        form = MovieForm({
            "title": "Blade Runner",
            "director": "Ridley Scott",
            "genre": "Science Fiction",
            "description": "I've seen things you people wouldn't believe. Attack ships on fire off the shoulder of Orion. I watched C-beams glitter in the dark near the Tannhauser Gate. All those moments will be lost in time, like tears in rain. Time to die.",
            "rating": 4,
            "imdb_link": "https://www.imdb.com/title/tt0083658/",
        })
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = MovieForm()
        self.assertEqual(form.Meta.fields, ['title', 'director', 'genre', 'description', 'rating', 'watched', 'imdb_link'])
