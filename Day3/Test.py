# Import necessary classes
from Person import Person
from Employee import Employee
from Car import Car
from Office import Office

# create Person
person1 = Person(name="Hamdy", money=5000, mood="happy", healthRate=90)
print(f"Person Created: {person1.name}, Money: {person1.money}, Mood: {person1.mood}, Health: {person1.healthRate}")

# Test Person Methods
print("\nTesting Person methods:")
print("Sleeping 6 hours:", person1.sleep(6))
print("Eating 2 meals:", person1.eat(2))
print("Buying 3 items:", person1.buy(3))

# create car
car1 = Car(name="Toyota", fuelRate=80, velocity=60)
print(f"\nCar Created: {car1.name}, Fuel Rate: {car1.fuelRate}, Velocity: {car1.velocity}")

# Create an Employee (inherits from Person)
employee1 = Employee(id=101, car=car1, email="hamdy@example.com", salary=2000, distanceToWork=10)
print(f"\nEmployee Created: {employee1.id}, Email: {employee1.email}, Salary: {employee1.salary}, Distance to Work: {employee1.distanceToWork}")

# Test Employee Methods
print("\nTesting Employee methods:")
employee1.work()
print("After Work, Salary:", employee1.salary)

employee1.drive(distance=10, velocity=50)
print("After Driving, Car Fuel Rate:", employee1.car.fuelRate)

employee1.refuel(20)
print("After Refueling, Car Fuel Rate:", employee1.car.fuelRate)

# Create an Office
office = Office(name="Tech Corp")
print(f"\nOffice Created: {office.name}")

# Test Office Methods
office.hire(employee1)
print("Employees in Office:", [emp.id for emp in office.get_all_employees()])

office.reward(empId=101, reward=500)
print(f"After Reward, Employee Salary: {employee1.salary}")

office.deduct(empId=101, deduction=200)
print(f"After Deduction, Employee Salary: {employee1.salary}")

# office.check_lateness(empId=101, moveHour=8)
# print(f"After Lateness Check, Employee Salary: {employee1.salary}")

office.fire(empId=101)
print("Employees in Office After Firing:", [emp.id for emp in office.get_all_employees()])
