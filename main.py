import json
from datetime import datetime
from plyer import notification
from typing import List
from pathlib import Path
from abc import ABC, abstractmethod

DATA_FILE = Path("data/birthdays.json")

# --- Models ---
class Person:
    def __init__(self, name: str, birthdate: str):
        self.name = name
        self.birthdate = birthdate  # Format: YYYY-MM-DD

    def is_birthday_today(self) -> bool:
        today = datetime.today().strftime("%m-%d")
        return self.birthdate[5:] == today

class User:
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.birthdays: List[Person] = []

    def add_birthday(self, person: Person):
        self.birthdays.append(person)

    def remove_birthday(self, name: str):
        self.birthdays = [p for p in self.birthdays if p.name.lower() != name.lower()]

# --- Abstraction ---
class Notifier(ABC):
    @abstractmethod
    def send(self, title: str, message: str):
        pass

# --- Singleton Notification Service ---
class NotificationService(Notifier):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotificationService, cls).__new__(cls)
        return cls._instance

    def send(self, title: str, message: str):
        notification.notify(
            title=title,
            message=message,
            timeout=10
        )

# --- Manager ---
class BirthdayManager:
    def __init__(self):
        self.users: dict[str, User] = {}
        self.notifier = NotificationService()
        self.load_data()

    def add_user(self, user: User):
        self.users[user.user_id] = user

    def get_user(self, user_id: str) -> User:
        return self.users.get(user_id)

    def check_birthdays_today(self):
        for user in self.users.values():
            for person in user.birthdays:
                if person.is_birthday_today():
                    self.notifier.send(
                        title=f"Birthday Reminder for {user.name}",
                        message=f"Today is {person.name}'s birthday! 🎉"
                    )

    def save_data(self):
        data = {
            uid: {
                "name": user.name,
                "birthdays": [
                    {"name": p.name, "birthdate": p.birthdate} for p in user.birthdays
                ]
            } for uid, user in self.users.items()
        }
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if not DATA_FILE.exists():
            return
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            for uid, info in data.items():
                user = User(uid, info['name'])
                for b in info['birthdays']:
                    user.add_birthday(Person(b['name'], b['birthdate']))
                self.users[uid] = user

# --- CLI Interface ---
def main():
    manager = BirthdayManager()
    while True:
        print("\nBirthday Reminder App")
        print("1. Add User")
        print("2. Add Birthday")
        print("3. Remove Birthday")
        print("4. Show Birthdays")
        print("5. Check Today's Birthdays")
        print("6. Save & Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            uid = input("User ID: ")
            name = input("Name: ")
            manager.add_user(User(uid, name))

        elif choice == '2':
            uid = input("User ID: ")
            user = manager.get_user(uid)
            if user:
                name = input("Friend's Name: ")
                date = input("Birthdate (YYYY-MM-DD): ")
                user.add_birthday(Person(name, date))
            else:
                print("User not found.")

        elif choice == '3':
            uid = input("User ID: ")
            user = manager.get_user(uid)
            if user:
                name = input("Friend's Name to Remove: ")
                user.remove_birthday(name)
            else:
                print("User not found.")

        elif choice == '4':
            uid = input("User ID: ")
            user = manager.get_user(uid)
            if user:
                for p in user.birthdays:
                    print(f"{p.name} - {p.birthdate}")
            else:
                print("User not found.")

        elif choice == '5':
            manager.check_birthdays_today()

        elif choice == '6':
            manager.save_data()
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()
