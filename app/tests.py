import unittest
from django.test import TestCase, Client
from django.urls import reverse
from . import views

class TestAppViews(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')

    def test_get_weather_view(self):
        city = 'London'
        response = self.client.post(reverse('get_weather'), {'city_name': city})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')
        self.assertEqual(response.context['weather']['location'], city)

    def test_city_autocomplete_view(self):
        term = 'Lon'
        response = self.client.get(reverse('city_autocomplete'), {'term': term})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertIn('London', response.json())

    def test_invalid_city_name(self):
        city = 'InvalidCity'
        response = self.client.post(reverse('get_weather'), {'city_name': city})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')
        self.assertEqual(response.context['weather']['error'], 'City not found')

class TestAppModels(TestCase):
    def test_city_list(self):
        self.assertIn('London', views.city_list)
        self.assertIn('Paris', views.city_list)
        self.assertIn('Berlin', views.city_list)

if __name__ == '__main__':
    unittest.main()