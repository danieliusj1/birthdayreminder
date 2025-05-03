import json #used for the birthday storing
from typing import Dict
from .models import User, Person #imported from models.py
from .notifier import NotificationService #service used for notifications from notifier.py
from .constants import DATA_FILE #where to store information

class BirthdayManager: #main class responsible for managing users and birthdays
    def __init__(self):
        self.users: Dict[str, User] = {}
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
