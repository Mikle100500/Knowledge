def find_car(cars, needed):

    returned_cars = []

    for car in cars:

        if car.startswith(needed):
            returned_cars.append(car)
    return returned_cars

