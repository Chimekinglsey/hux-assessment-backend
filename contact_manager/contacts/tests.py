import unittest
import requests
import time


class UserRegistrationTestCase(unittest.TestCase):
    """ Tests for User creation """
    def test_user_registration_success(self):
        # Test case for successful user registration
        response = requests.post('http://localhost:8000/auth/register/', json={'username': 'testuser3', 'password': 'easypassword'})
        self.assertEqual(response.status_code, 201)

    def test_user_registration_invalid_data(self):
        # Test case for registration with invalid data
        response = requests.post('http://localhost:8000/auth/register/', json={'username': '', 'password': 'password'})
        self.assertEqual(response.status_code, 400)


class CreateContactTestCase(unittest.TestCase):    
    """ Tests for the Create Contact API endpoint"""
    def setUp(self):
        # Delay execution by 2 seconds
        time.sleep(2)
        # Obtain JWT token by logging in or registering a user
        response = requests.post('http://localhost:8000/api/token/', json={'username': 'testuser3', 'password': 'easypassword'})
        self.token = response.json().get('access')

    def test_create_contact_success(self):
        # Test case for successful creation of a contact with authentication
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.post('http://localhost:8000/create-contact/', json={'first_name': 'John', 'last_name': 'Doe', 'phone_number': '1234567890'}, headers=headers)
        self.assertEqual(response.status_code, 201)
    
    def test_create_contact_invalid_data(self):
        # Test case for creating a contact with invalid data with authentication
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.post('http://localhost:8000/create-contact/', json={'first_name': '', 'last_name': 'Doe', 'phone_number': '1234567890'}, headers=headers)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())


class UpdateContactTestCase(unittest.TestCase):
    """ Tests for the Update Contact API endpoint"""
    @unittest.expectedFailure
    def test_update_contact_success(self):
        # Test case for successful update of a contact
        # Request to the Update Contact endpoint with test data
        # Because the id of 1 is not created by this user, it is expected to fail
        response = requests.put('http://localhost:8000/update-contact/1/', json={'first_name': 'Updated', 'last_name': 'Doe', 'phone_number': '1234567890'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['first_name'], 'Updated') 

    def test_update_contact_not_found(self):
        # Test case for updating a contact that does not exist
        # Make a request to update a non-existent contact
        response = requests.put('http://localhost:8000/update-contact/100/', json={'first_name': 'Updated', 'last_name': 'Doe', 'phone_number': '1234567890'})
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json())  # Assuming the response contains an error message

if __name__ == '__main__':
    unittest.main()
