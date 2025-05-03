from datetime import datetime
from typing import List

class Person:
    def __init__(self, name: str, birthdate: str):
        # Expected birthdate format: YYYY-MM-DD
        if len(birthdate) != 10 or birthdate[4] != '-' or birthdate[7] != '-':
            raise ValueError("Birthdate must be in format YYYY-MM-DD")
        self.name = name
        self.birthdate = birthdate

    def is_birthday_today(self) -> bool:
        today = datetime.today().strftime("%m-%d")
        return self.birthdate[5:] == today

class User:
    def __init__(self, user_id: str, name: str):
        #encapsulation example - fields like self.birthdays and self.name are encapsulated inside the project
        self.user_id = user_id
        self.name = name
        self.birthdays: List[Person] = []

    def add_birthday(self, person: Person):
        self.birthdays.append(person)
        #the access to birthday list is controlled using the method above and below - direct data manipulation is prevented outside the class interface
    def remove_birthday(self, name: str):
        self.birthdays = [p for p in self.birthdays if p.name.lower() != name.lower()]
