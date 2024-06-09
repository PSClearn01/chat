import unittest
from unittest.mock import patch
from django.test import RequestFactory
from .views import index

class TestViews(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index(self):
        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    @patch('requests.post')
    def test_api_call(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = '{"response": "Hello, world!"}'

        request = self.factory.get('/')
        response = index(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'response': 'Hello, world!'})

        mock_post.assert_called_once_with(
            "https://api.edenai.run/v2/text/chat",
            json={
                "temperature": 0,
                "max_tokens": 1000,
                "providers": ["anthropic/claude-instant-v1"]
            },
            headers={
                "accept": "application/json",
                "content-type": "application/json",
                "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiOWM2YTZhY2ItYjVkYi00NTNmLWE1ZTctMTQ3ZTg4NjdhNjEyIiwidHlwZSI6InNhbmRib3hfYXBpX3Rva2VuIn0.jPRbf3i3rGWj_I3n0ekr8CQFF6BOZbEzZN1krVtJtnE"
            }
        )

if __name__ == '__main__':
    unittest.main()