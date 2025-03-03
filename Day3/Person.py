# import smtplib
# import os
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
#
# class Person:
#     '''- attributes (name, money, mood, healthRate).
#     - methods (sleep, eat, buy, work, send_email).'''
#     moods = ('happy', 'tired', 'lazy')
#
#     def __init__(self, name, money, mood, healthRate):
#         self.name = name
#         self.money = money
#
#         if mood in self.__class__.moods:
#             self.mood = mood
#         else:
#             raise ValueError(f"Invalid mood: {mood}. Choose from {self.__class__.moods}")
#
#         if 0 <= healthRate <= 100:
#             self.healthRate = healthRate
#         else:
#             raise ValueError(f"Invalid health rate: {healthRate}. Must be between 0 and 100.")
#
#     def sleep(self, hour):
#         #__class__ -> it refer to the class instance moods
#         if hour < 7:
#             self.mood = self.__class__.moods[1]  # tired
#         elif hour > 7:
#             self.mood = self.__class__.moods[2]  # lazy
#         else:
#             self.mood = self.__class__.moods[0]  # happy
#         return self.mood
#
#     def eat(self, meals):
#         if meals == 3:
#             self.healthRate = 100
#         elif meals == 2:
#             self.healthRate = 75
#         elif meals == 1:
#             self.healthRate = 50
#         else:
#             return "Invalid number of meals"
#         return self.healthRate
#
#     def buy(self, item_count):
#         self.money -= item_count * 10
#         return self.money
#
#     def work(self, hour):
#         if hour < 8:
#             self.mood = self.__class__.moods[2]  # lazy
#         elif hour > 8:
#             self.mood = self.__class__.moods[1]  # tired
#         else:
#             self.mood = self.__class__.moods[0]  # happy
#         return self.mood
#
#     def send_email(self, to, subject, msg, receiver_name):
#         sender_email = os.getenv("SENDER_EMAIL")
#         sender_password = os.getenv("SENDER_PASSWORD")
#
#         if not sender_email or not sender_password:
#             print("Error: Email credentials not set.")
#             return
#
#         message = MIMEMultipart()
#         message['From'] = sender_email
#         message['To'] = to
#         message['Subject'] = subject
#
#         email_body = f"Dear {receiver_name},\n\n{msg}\n\nBest regards,\n{self.name}"
#         message.attach(MIMEText(email_body, 'plain'))
#
#         try:
#             server = smtplib.SMTP("smtp.ex.c", 587)
#             server.starttls()
#             server.login(sender_email, sender_password)
#             server.send_message(message)
#             server.quit()
#             print("Email sent successfully!")
#         except Exception as e:
#             print(f"Error sending email: {e}")
###if with DB connection###
from database import Base, engine, session
from sqlalchemy import Column, Integer, String, Float

class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    money = Column(Float, nullable=False)
    mood = Column(String, nullable=False)
    healthRate = Column(Integer, nullable=False)

    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def save_to_db(self):
        session.add(self)
        session.commit()

# Create tables in DB
Base.metadata.create_all(engine)
