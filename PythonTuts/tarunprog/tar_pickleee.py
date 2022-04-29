import pickle

# car = ["BMW", "Ford", "Audi", "Mustang", "chevrolet"]
# file_name = "t_car.pkl"
# file_obj = open(file_name, 'wb')
# pickle.dump(car, file_obj)
# file_obj.close()
#
file = "t_car.pkl"
file_obj = open(file, "rb")
my_car = pickle.load(file_obj)
print((my_car))
print(type(my_car))
