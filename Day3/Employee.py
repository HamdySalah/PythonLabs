# import re
# class Employee:
#     '''
#     Employee Class (is a Person):
#     - attributes (id, car, email, salary, distanceToWork)
#     - methods (work, drive, refuel, send_mail)
#     '''
    # def __init__(self, id, car, email, salary, distanceToWork):
    #     self.id = id
    #     self.car = car
    #     # Validate email format
    #     if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
    #         self.email = email
    #     else:
    #         raise ValueError(f"Invalid email address: {email}")
    #     # Validate salary
    #     if salary >= 1000:
    #         self.salary = salary
    #     else:
    #         raise ValueError("Salary must be at least 1000.")
    #     self.distanceToWork = distanceToWork
    #
    # def work(self):
    #     self.salary += self.distanceToWork
    #
    # def drive(self, distance, velocity):
    #     '''Order the car to run with given distance and velocity.'''
    #     if self.car.fuelRate > 0:
    #         self.car.run(velocity, distance)
    #     else:
    #         print("Car has no fuel. Please refuel.")
    #
    # def refuel(self, gasAmount=100):
    #     '''Add gasAmount to the car's fuel rate.'''
    #     if 0 <= self.car.fuelRate + gasAmount <= 100:
    #         self.car.fuelRate += gasAmount
    #         print(f"Car refueled. New fuel level: {self.car.fuelRate}%")
    #     else:
    #         print("Invalid fuel amount. Fuel must be between 0 and 100.")
    #
    # def send_mail(self):
    #     self.salary += self.distanceToWork
###if there's DB connection
from database import Base, session, engine
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    person_id = Column(Integer, ForeignKey('persons.id'))
    email = Column(String, unique=True, nullable=False)
    salary = Column(Float, nullable=False)
    distanceToWork = Column(Float, nullable=False)

    person = relationship("Person")

    def __init__(self, person_id, email, salary, distanceToWork):
        self.person_id = person_id
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def save_to_db(self):
        session.add(self)
        session.commit()
