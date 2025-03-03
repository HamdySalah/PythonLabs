#
# from Employee import Employee
# class Office:
#     '''Represents an office that manages employees.
#
#     Attributes:
#         - name: Office name
#         - employees: List of Employee objects
#         - employeesNum (class variable): Tracks total employees across all offices.
#     '''
#
#     employeesNum = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.employees = []
#
#     def get_all_employees(self):
#         '''Returns a list of all employees.'''
#         return self.employees
#
#     def get_employee(self, empId):
#         '''Returns an employee object by ID.'''
#         for emp in self.employees:
#             if emp.id == empId:
#                 return emp
#         return None  # Employee not found
#
#     def hire(self, employee):
#         '''Hires an employee and adds them to the list.'''
#         if isinstance(employee, Employee):
#             self.employees.append(employee)
#             Office.employeesNum += 1
#         else:
#             print("Invalid employee object.")
#
#     def fire(self, empId):
#         '''Fires an employee by removing them from the list.'''
#         employee = self.get_employee(empId)
#         if employee:
#             self.employees.remove(employee)
#             Office.employeesNum -= 1
#             print(f"Employee {empId} fired.")
#         else:
#             print(f"Employee {empId} not found.")
#
#     def deduct(self, empId, deduction):
#         '''Deducts money from an employee’s salary.'''
#         employee = self.get_employee(empId)
#         if employee:
#             if employee.salary >= deduction:
#                 employee.salary -= deduction
#                 print(f"Deducted {deduction} from Employee {empId}. New salary: {employee.salary}")
#             else:
#                 print("Deduction amount exceeds salary.")
#         else:
#             print("Employee not found.")
#
#     def reward(self, empId, reward):
#         '''Adds money to an employee’s salary.'''
#         employee = self.get_employee(empId)
#         if employee:
#             employee.salary += reward
#             print(f"Rewarded {reward} to Employee {empId}. New salary: {employee.salary}")
#         else:
#             print("Employee not found.")
#
#     def check_lateness(self, empId, moveHour, targetHour=9):
#         '''Checks if an employee is late and applies rewards or deductions accordingly.'''
#         employee = self.get_employee(empId)
#         if employee:
#             is_late = self.calculate_lateness(targetHour, moveHour, employee.distanceToWork, employee.car.velocity)
#             if is_late:
#                 self.deduct(empId, 10)
#                 print(f"Employee {empId} was late. -10 deducted.")
#             else:
#                 self.reward(empId, 10)
#                 print(f"Employee {empId} was on time. +10 rewarded.")
#         else:
#             print("Employee not found.")
#
#     @staticmethod
#     def calculate_lateness(targetHour, moveHour, distance, velocity=1):
#         '''Determines if an employee will be late based on travel time.'''
#         travel_time = distance / velocity  #
#         arrival_time = moveHour + travel_time
#         return arrival_time > targetHour
#
#     @classmethod
#     def change_emps_num(cls, num):
#         '''Modifies the number of employees across all offices.'''
#         cls.employeesNum = num
#         print(f"Total employees updated to: {cls.employeesNum}")

###if there's DB connection
from database import Base, session, engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Office(Base):
    __tablename__ = 'offices'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def save_to_db(self):
        session.add(self)
        session.commit()

Base.metadata.create_all(engine)
