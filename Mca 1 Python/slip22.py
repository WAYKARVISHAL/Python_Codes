# # Q.2 Create class Vehicle having attributes type, model. The class Car is vehicle having
# # attributes cname, cost. The class Truck is a vehicle having attributes tname, cost.
# # Display all information about light and heavy vehicle. 

# Base class
class Vehicle:
    def __init__(self, vehicle_type, model):
        self.vehicle_type = vehicle_type
        self.model = model

    def display_vehicle_info(self):
        print(f"Vehicle Type: {self.vehicle_type}, Model: {self.model}")


# Derived class for Car
class Car(Vehicle):
    def __init__(self, vehicle_type, model, cname, cost):
        super().__init__(vehicle_type, model)
        self.cname = cname
        self.cost = cost

    def display_info(self):
        self.display_vehicle_info()
        print(f"Car Name: {self.cname}, Cost: {self.cost}")


# Derived class for Truck
class Truck(Vehicle):
    def __init__(self, vehicle_type, model, tname, cost):
        super().__init__(vehicle_type, model)
        self.tname = tname
        self.cost = cost

    def display_info(self):
        self.display_vehicle_info()
        print(f"Truck Name: {self.tname}, Cost: {self.cost}")


# Instances and displaying information
# Light Vehicle - Car
car = Car(vehicle_type="Light Vehicle", model="2024", cname="Honda City", cost=1500000)
print("Car Details:")
car.display_info()

print("\n")

# Heavy Vehicle - Truck
truck = Truck(vehicle_type="Heavy Vehicle", model="2024", tname="Ashok Leyland", cost=2500000)
print("Truck Details:")
truck.display_info()

# Q. 1 Write a lambda expression to find square of all elements in the list. 
ab=[1,2,3,5]
c=list(map(lambda x:x*2,ab))
print(c)