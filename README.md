# Birthday Reminder App Report

## 1. Introduction

The **Birthday Reminder App** is a Python-based application designed to help users manage and track birthdays. The app provides functionalities to add, remove, and display birthdays for multiple users, as well as send notifications on the day of the birthday. Additionally, the app saves and loads birthday data to/from a JSON file, ensuring data persistence between sessions.

### 1.1. How to launch it

The launching process includes some command work and requires to have Python installed on the user's computer. The user needs to **open powershell in the program directory and execute the following command**: `python main.py`. There is an executable called `main.exe` in the `dist` folder, however, the program **does not send out notifications** when opened using the `.exe`.
## 2. Features

- **Add Users**: Users can be added to the system, each with their own set of birthdays.
- **Add Birthdays**: Birthdays can be associated with users, which include a name and birthdate.
- **Remove Birthdays**: Users can remove birthdays from their list.
- **View Birthdays**: Users can view all birthdays associated with them.
- **Check Today's Birthdays**: The app checks and sends notifications for birthdays that occur on the current day.
- **Data Persistence**: Birthday data is saved to and loaded from a `birthdays.json` file.
- **Notifications**: The app sends desktop notifications on the day of each birthday using the **`plyer`** library.

## 3. Object-Oriented Programming (OOP) Principles

The app is built using **Object-Oriented Programming** principles, which provide a clear and organized structure for the code. The following OOP principles are demonstrated in the application:

### 3.1. Abstraction
- The **Notifier** class defines an abstract class `Notifier` in `notifier.py`, which enforces a method `send` that subclasses must implement. This abstracts the notification mechanism.

### 3.2. Polymorphism
- The **NotificationService** class inherits from `Notifier` and implements the `send` method, using the `plyer.notification` module to send notifications. This allows for future extension to use different notification mechanisms without changing the app's core logic.

### 3.3. Inheritance
- The `NotificationService` class inherits from `Notifier`, which is an abstract base class. This ensures that all notification services adhere to the same interface and can be swapped out for different implementations.

### 3.4. Encapsulation
- The `User` and `Person` classes in `models.py` encapsulate data such as `name` and `birthdate`. These fields are protected and accessed through class methods to ensure data integrity and proper management.

## 4. Design Pattern Used

### Singleton Design Pattern
- The **NotificationService** class implements the **Singleton pattern**, which ensures that only **one instance** of the notification service is created throughout the application's lifecycle. This guarantees a centralized control for sending notifications and prevents unnecessary duplication of the service.

```python
class NotificationService(Notifier):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotificationService, cls).__new__(cls)
        return cls._instance
```

## 5. Testing

The **Birthday Reminder App** has been thoroughly tested using Python's **`unittest`** framework to ensure that all features work as expected. These tests cover the addition/removal of users and birthdays, checking for birthdays on the current day, saving/loading data, and more.

Additionally, an **executable** (.exe) file has been created using **PyInstaller**. This executable makes it easier to launch the testing experience without the need for running Python commands in PowerShell or the terminal. Instead of using the `python test_main.py` command, users can **double-click the `run_tests.exe` file** inside of the *dist* folder to run the app. The executable provides a more user-friendly experience, especially for those who are not familiar with command-line usage.

### 5.1. Test Coverage
The unit tests cover the following functionalities:
- **Adding and Removing Users**: Tests ensure that users can be added and removed correctly.
- **Adding and Removing Birthdays**: The app correctly adds and removes birthdays for users.
- **Saving and Loading Data**: The app saves and loads birthday data to/from the `birthdays.json` file, ensuring data persistence.
- **Birthday Notifications**: The app correctly checks for birthdays today and sends notifications.
- **Invalid Date Handling**: The app raises an error if an invalid date format is provided.
- **Duplicate User Handling**: The app ensures that users with duplicate IDs are replaced correctly.

### 5.2. Running the Tests
Tests are executed using the following command:
```bash
python -m unittest test_main.py
```
Or by simply **launching a custom `run_tests.exe` file** which runs all of these tests **automatically**. 

### 5.3. Example Output
Running the tests will output results like:
```
test_add_user_and_birthday (test_main.TestBirthdayApp) ... ok
test_remove_birthday (test_main.TestBirthdayApp) ... ok
test_save_and_load_data (test_main.TestBirthdayApp) ... ok
test_birthday_today (test_main.TestBirthdayApp) ... ok
----------------------------------------------------------------------
Ran 7 tests in 0.023s

OK
```

## 6. Future Enhancements

### 6.1. Graphical User Interface (GUI)
- The app currently runs in the terminal. A **GUI** could be developed using **Tkinter** or **PyQt5** to make the app more user-friendly.

### 6.2. Multi-Language Support
- The app could be extended to support notifications in multiple languages.

### 6.3. Cloud Synchronization
- The app could be extended to synchronize birthday data across devices using cloud services.

## 7. Conclusion

The **Birthday Reminder App** successfully meets the requirements of the project by implementing essential features such as birthday management, notifications, and data persistence. The use of **OOP principles** and the **Singleton design pattern** ensures that the app is maintainable and scalable. Unit tests validate the functionality and ensure the app behaves as expected. Future improvements could include a **GUI** and additional features for synchronization and language support.
