from django.test import TestCase
from django.test import Client

# Create your tests here.
class HttpRunWatchlistTest(TestCase):

    def test_mywatchlist(self):
        response  = Client().get('/mywatchlist/')
        self.assertEqual(response.status_code, 200)
    
    def test_html_mywatchlist(self):
        response  = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    
    def test_json_mywatchlist(self):
        response  = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
    
    def test_xml_mywatchlist(self):
        response  = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)