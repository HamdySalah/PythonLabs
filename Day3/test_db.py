from Person import Person
from Employee import Employee
#
# Create a new Person
person1 = Person(name="Alice", money=5000, mood="happy", healthRate=90)
person1.save_to_db()
#
# Create an Employee linked to this Person
employee1 = Employee(person_id=person1.id, email="alice@example.com", salary=2000, distanceToWork=10)
employee1.save_to_db()

print("Data saved to database successfully!")
