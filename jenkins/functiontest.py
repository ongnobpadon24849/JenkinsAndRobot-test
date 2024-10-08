import unittest
from flask import Flask
from flask_api.app import app 

class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        print(f"Test(index) ==> Response: {response.data.decode('utf-8')}")

    def test_getcode(self):
        tester = app.test_client(self)
        response = tester.get('/getcode')
        self.assertEqual(response.status_code, 200)
        print(f"Test(/getcode) ==> Response: {response.data.decode('utf-8')}")

    def test_plus_valid(self):
        tester = app.test_client(self)
        response = tester.get('/plus/3/4')
        self.assertEqual(response.status_code, 200)
        self.assertIn('plus', response.data.decode('utf-8'), 7)
        print(f"Test(/plus/3/4) ==> Response: {response.data.decode('utf-8')}")

        response = tester.get('/plus/5.5/9.6')
        self.assertEqual(response.status_code, 200)
        self.assertIn('plus', response.data.decode('utf-8'), 15.1)
        print(f"Test(/plus/5.5/9.6) ==> Response: {response.data.decode('utf-8')}")

    def test_plus_invalid(self):
        tester = app.test_client(self)
        response = tester.get('/plus/3/abc')
        self.assertEqual(response.status_code, 200)
        self.assertIn('ERROR', response.data.decode('utf-8'), 'Invalid input')
        print(f"Test(/plus/3/abc) ==> Response: {response.data.decode('utf-8')}")

        response = tester.get('/plus/abc/def')
        self.assertEqual(response.status_code, 200)
        self.assertIn('ERROR', response.data.decode('utf-8'), 'Invalid input')
        print(f"Test(/plus/abc/def) ==> Response: {response.data.decode('utf-8')}")

        response = tester.get('/plus/5.5.4.4/9.9.6.6')
        self.assertEqual(response.status_code, 200)
        self.assertIn('ERROR', response.data.decode('utf-8'), 'Invalid input')
        print(f"Test(/plus/5.5.4.4/9.9.6.6) ==> Response: {response.data.decode('utf-8')}")

if __name__ == '__main__':
    unittest.main()
