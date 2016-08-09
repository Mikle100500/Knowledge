import unittest

from cars.cars_list_conditions import find_car

cars_list = ["BMW M5", "BMW M3", "Porsche 911BMW", "Mercedes G63", "Morgan Aero", "Alpha Romeo Julette"]


class TestCarsList(unittest.TestCase):
    def test_cars_list(self):
        self.assertEqual(find_car(cars_list, "BMW"), ["BMW M5", "BMW M3"])
        self.assertEqual(find_car(cars_list, "Porsche"), ["Porsche 911BMW"])
        self.assertEqual(find_car(cars_list, "Alpha Romeo"), ["Alpha Romeo Julette"])


if __name__ == '__main__':
    unittest.main()
