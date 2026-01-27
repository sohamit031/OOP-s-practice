class Car:
    def move(self):
        return 'drive'

class Plane:
    def move(self):
        return 'fly'
    
car=Car()
plane=Plane()

my_vehicles= [car,plane]

for vehicle in my_vehicles :
    print(vehicle.move())

