import unittest

from class_cars import find_car, Car

cars_list = [
    Car("BMW", "M5"),
    Car("BMW", "M3"),
    Car("Porsche", "911"),
    Car("Mercedes", "G63"),
    Car("Morgan", "Aero"),
    Car("Alpha Romeo", "Julette"),
]


class TestCarsList(unittest.TestCase):
    def test_cars_list(self):
        self.assertEqual(find_car(cars_list, "BMW"), [Car("BMW", "M5"),  Car("BMW", "M3")])
        self.assertEqual(find_car(cars_list, "Porsche"), Car("Porsche", "911"))
        self.assertEqual(find_car(cars_list, "Alpha Romeo"), Car("Alpha Romeo", "Julette"))


if __name__ == '__main__':
    unittest.main()