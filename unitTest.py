import unittest
import requests
from main import print_channel_data, data_to_dataframe

class unitTest(unittest.TestCase):
    def setUp(self):
      #Get Good Data
      r = requests.get(f'https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&forUsername=Vsauce&key=AIzaSyCjRbmEAeEe35cuqAsoJ7Zn80ukUx0FQjQ')
      self.good_data = r.json()

      #Get Bad Data
      r = requests.get(f'https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&forUsername=ThisIsNotARealChannelName&key=AIzaSyCjRbmEAeEe35cuqAsoJ7Zn80ukUx0FQjQ')
      self.bad_data = r.json()

    def test_print_channel_data(self):
        self.assertEqual(print_channel_data(self.good_data), True)
        self.assertEqual(print_channel_data(self.bad_data), False)

    def test_data_to_dataframe(self):
        self.assertEqual(data_to_dataframe(self.bad_data), False)

if __name__ == '__main__':
    unittest.main()