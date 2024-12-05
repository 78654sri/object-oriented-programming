class Car:
    def info(self):
        print("i am a car")
class Bike:
    def info(self):
        print("i am a bike")

car=Car()
bike=Bike()


for vehicle in(car,bike):
    vehicle.info()

