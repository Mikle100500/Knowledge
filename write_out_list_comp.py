from class_cars import Car, find_car

def write_out_needed_cars(needed_car):
    output = open('output_cars.txt', 'w')
    saved_car_store = []

    for car_line in open('input_cars.txt'):
        data = car_line.split(';')
        vendor, name = data
        saved_car = Car(vendor, name)
        saved_car_store.append(saved_car)
        [car for car in saved_car_store if car.vendor == needed_car]

write_out_needed_cars("BMW")

    # for each_saved_car in find_car(saved_car_store, needed_car):
    #     output.write(each_saved_car.vendor + ';' + each_saved_car.name)


# def find_car(cars, needed):
#
#     returned_cars = []
#
#     for car in cars:
#         if car.vendor == needed:
#             returned_cars.append(car)
#     return returned_cars