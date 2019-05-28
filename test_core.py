from bovespa import app
import unittest

class TestHomeView(unittest.TestCase):

    def setUp(self):
        app_test = app.test_client()
        self.response = app_test.get('/')
        self.result = app_test.get('/result')

    # Testa se a resposta é 200 ("ok")
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    # Testa se o content_type da resposta da home esta correto
    # -- deve retornar um html
    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    # Testa se o retorno da página "result" está correto 
    # -- deve retornar um html
    def test_result_type(self):
        self.assertIn('text/html', self.result.content_type)

if __name__ == '__main__':
    unittest.main()