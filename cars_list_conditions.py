def find_car(cars, needed):
    returned_cars = []
    for car in cars:
        if car[0: len(needed)] == needed:
            returned_cars.append(car)
    return returned_cars
