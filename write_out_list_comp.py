from class_cars import Car, find_car


def write_out_needed_cars(needed_car):
    output = open('output_cars.txt', 'w')
    saved_car_store = []

    for car_line in open('input_cars.txt'):
        data = car_line.split(';')
        vendor, name = data
        saved_car = Car(vendor, name)
        saved_car_store.append(saved_car)
        if saved_car in find_car(saved_car_store, needed_car):
            output.write(str(saved_car.vendor + ';' + saved_car.name))


def find_car(cars, needed):
    return [car for car in cars if car.vendor == needed]


write_out_needed_cars("Tesla")