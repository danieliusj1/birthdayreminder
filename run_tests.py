import unittest
import time
from test_main import TestBirthdayApp

if __name__ == "__main__":
    with open("test_results.txt", "w") as result_file:
        # Create a custom runner to redirect output to the file
        runner = unittest.TextTestRunner(result_file, verbosity=2)

        # Record start time
        start_time = time.time()

        # Run the tests
        unittest.main(testRunner=runner, verbosity=2)

        # Calculate and log the time taken for the tests
        end_time = time.time()
        time_taken = end_time - start_time

        result_file.write(f"\n\nTotal time taken: {time_taken:.4f} seconds\n")
