import unittest
import os
from datetime import datetime
from core.models import Person, User
from core.manager import BirthdayManager, DATA_FILE

class TestBirthdayApp(unittest.TestCase):

    def setUp(self):
        """Prepare a clean manager and delete data file if it exists."""
        self.manager = BirthdayManager()
        self.manager.users = {}
        if DATA_FILE.exists():
            os.remove(DATA_FILE)

    def test_add_user_and_birthday(self):
        """Test adding a user and birthday to the system."""
        user = User("user1", "Alice")
        person = Person("Bob", "2000-01-01")
        user.add_birthday(person)
        self.manager.add_user(user)
        self.assertIn("user1", self.manager.users)
        self.assertEqual(len(self.manager.get_user("user1").birthdays), 1)
        self.assertEqual(self.manager.get_user("user1").birthdays[0].name, "Bob")

    def test_remove_birthday(self):
        """Test removing a birthday from a user's list."""
        user = User("user2", "Charlie")
        user.add_birthday(Person("Dave", "1990-05-01"))
        user.remove_birthday("Dave")
        self.assertEqual(len(user.birthdays), 0)

    def test_save_and_load_data(self):
        """Test saving to and loading from the JSON file."""
        user = User("user3", "Eve")
        user.add_birthday(Person("Frank", "1999-09-09"))
        self.manager.add_user(user)
        self.manager.save_data()

        # Reload
        new_manager = BirthdayManager()
        reloaded_user = new_manager.get_user("user3")
        self.assertIsNotNone(reloaded_user)
        self.assertEqual(reloaded_user.name, "Eve")
        self.assertEqual(len(reloaded_user.birthdays), 1)
        self.assertEqual(reloaded_user.birthdays[0].name, "Frank")

    def test_birthday_today(self):
        """Test if birthday matches today's date."""
        today = datetime.today().strftime("%Y-%m-%d")
        person = Person("Grace", today)
        self.assertTrue(person.is_birthday_today())

    def test_invalid_date_format(self):
        """Test handling of incorrectly formatted dates."""
        user = User("user4", "Hank")
        with self.assertRaises(ValueError):
            Person("Ivy", "01-01-2000")

    def test_duplicate_user_id(self):
        """Test that adding a user with duplicate ID replaces the old one."""
        user1 = User("user5", "Jane")
        user2 = User("user5", "Kate")
        self.manager.add_user(user1)
        self.manager.add_user(user2)
        self.assertEqual(self.manager.get_user("user5").name, "Kate")

    def test_empty_birthday_list(self):
        """Ensure user with no birthdays still loads correctly."""
        user = User("user6", "Leo")
        self.manager.add_user(user)
        self.manager.save_data()

        new_manager = BirthdayManager()
        loaded = new_manager.get_user("user6")
        self.assertEqual(len(loaded.birthdays), 0)
        self.assertEqual(loaded.name, "Leo")

if __name__ == '__main__':
    unittest.main(verbosity=2)
