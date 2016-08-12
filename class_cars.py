class Car(object):
    def __init__(self, vendor, name):
        self.vendor = vendor
        self.name = name

    def __repr__(self):
        return "{} {}".format(self.vendor, self.name)

    def __eq__(self, entity):
        print(". . . O V E R L O A D E D. . .")
        if self.vendor == entity.vendor and self.name == entity.name:
            return True
        else:
            return False


def find_car(cars, needed):
    returned_cars = []

    for car in cars:
        if car.vendor == needed:
            returned_cars.append(car)
    return returned_cars
