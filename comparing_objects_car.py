from class_cars import Car

object_1 = Car("BMW", "X5")
object_2 = Car("BMW", "X5")


print(object_1 == object_2)

# def object_comparing(object_1, object_2):
#
#     if object_1.vendor == object_2.vendor and object_1.name == object_2.name:
#         return True
#     else:
#         return False

# def object_comparing(object_1, object_2):
#
#     if object_1 is object_2:
#         return True
#     else:
#         return False
#
# print(object_comparing(object_1, object_2))