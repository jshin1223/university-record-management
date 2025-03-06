"""
This script discovers and runs all unit tests inside the `tests` folder.
"""

import unittest

def run_tests():
    """Discovers and runs all test files in the 'tests' directory."""
    print("🧪 Running all tests...\n")
    loader = unittest.TestLoader()
    suite = loader.discover('tests')  # Discover all test files in the tests folder

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if result.wasSuccessful():
        print("\n✅ All tests passed successfully!")
        exit(0)
    else:
        print("\n❌ Some tests failed. Check the errors above.")
        exit(1)

if __name__ == "__main__":
    run_tests()
