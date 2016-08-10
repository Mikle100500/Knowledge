from class_cars import Car

def save_cars_to_file():
    save_cars_to_file = []

    for car_line in open('input_cars.txt'):
        data = car_line.split(';')
        vendor, name = data
        saved_car = Car(vendor, name)
        save_cars_to_file.append(saved_car)

    output = open('output_cars.txt', 'w')
    output.write(str(save_cars_to_file))