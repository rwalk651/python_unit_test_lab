import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    def test_single_item(self):
        princes = [1]
        expected_discount = 1
        self.assertEqual(expected_discount, discount(princes))


    def test_negative_prices(self):
        prices = [-99999999999999, -999999999995, 99999999999]
        expected_discount = -99999999999999
        self.assertEqual(expected_discount, discount(prices))


    def test_prices_in_dictionary(self):
        price = {'carrot': 2, 'donut': 4, 'banana': 1}
        expected_discount = 1
        self.fail('test')


if __name__ == '__main__':
    unittest.main()