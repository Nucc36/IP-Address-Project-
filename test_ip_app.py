import unittest
from unittest.mock import patch
from ip_address_code_final import get_ip_info

class TestIPApp(unittest.TestCase):
    '''test module to test get ip function in 'ip_address_code_final.py'''

    @patch("ip_address_code_final.requests.get")
    def test_successful_response(self, mock_get):
        
        #Mock successful API response of 200 and JSON response values
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
           "ip": "8.8.8.8",
           "city": "Sydney",
           "country": "AU"
        }
        #Runs the function and checks conditions
        result = get_ip_info()
        self.assertIsInstance(result, dict)
        self.assertIn("ip", result)
        self.assertEqual(result["city"], "Sydney")

    @patch("ip_address_code_final.requests.get")
    #Mocks API 429 rate limit. 
    def test_rate_limit(self, mock_get):
        mock_get.return_value.status_code = 429
        result = get_ip_info()
        #Function should return None
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()