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
    def test_bmw(self):
        filter_bmw = find_car(cars_list, "BMW")

        self.assertEquals(filter_bmw[0].vendor, "BMW")
        self.assertEquals(filter_bmw[0].name, "M5")

        self.assertEquals(filter_bmw[1].vendor, "BMW")
        self.assertEquals(filter_bmw[1].name, "M3")

    def test_porche(self):
        self.assertTrue(find_car(cars_list, "Porsche") == Car("Porsche", "911"))

    def test_alpha(self):
        self.assertTrue(find_car(cars_list, "Alpha Romeo") == Car("Alpha Romeo", "Julette"))

    def test_objects(self):
        assert find_car(cars_list, "BMW") == Car("BMW", "M5")


if __name__ == '__main__':
    unittest.main()