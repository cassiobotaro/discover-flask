from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        """Ensure that Flask was set up correctly."""
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        """Ensure that the login page loads correctly."""
        tester = app.test_client(self)
        response = tester.get('/login')
        self.assertIn(b'Please login', response.data)

    def test_correct_login(self):
        """Ensure login behaves correctly with correct credentials."""
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assertIn(b'You were logged in', response.data)

    def test_incorrect_login(self):
        """Ensure login behaves correctly with incorrect credentials."""
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username="wrong", password="wrong"),
            follow_redirects=True
        )
        self.assertIn(b'Invalid credentials. Please try again.', response.data)

    def test_logout(self):
        """Ensure logout behaves correctly."""
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You were logged out', response.data)

    def test_main_route_requires_login(self):
        """Ensure that main page requires user login."""
        tester = app.test_client()
        response = tester.get('/', follow_redirects=True)
        self.assertIn(b'You need to login first.', response.data)

    def test_logout_route_requires_login(self):
        """Ensure that logout page requires user login."""
        tester = app.test_client()
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You need to login first.', response.data)

    def test_posts_show_up_on_main_page(self):
        """Ensure that posts show up on the main page."""
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assertIn(b'Hello from the shell', response.data)


if __name__ == '__main__':
    unittest.main()
