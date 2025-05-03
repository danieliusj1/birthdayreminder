import unittest
#this one is so that the testing can be done by lauching an exe file rather than via the terminal
from test_main import TestBirthdayApp

if __name__ == "__main__":
    with open("test_results.txt", "w") as result_file:
        runner = unittest.TextTestRunner(result_file)
        unittest.main(testRunner=runner, verbosity=2)
