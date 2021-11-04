# View all of the functions for an object using dir
output = dir(5)
print(output)

# Object is a collection of data (variables) and methods that operate on data

# A class is a blueprint for one or more objects

# example

class Car:
    speed = 0
    started = False

    def start(self):
        self.started = True
        print("Car started, let's go!")

    def increase_speed(self, delta):
        if (self.started):
            self.speed = self.speed + delta
            print("Going faster!!")
        else:
            print ("You silly billy, you didn't start the car!")

    def stop(self):
        self.started = False
        self.speed = 0
        print("Stopping")

car = Car()
car.increase_speed(10)
car.start()
car.increase_speed(1000)
car.stop()
car.increase_speed(10)

# Each object in python has a unique identifier

print(id (car))
