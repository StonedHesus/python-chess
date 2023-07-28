"""
    This here module hosts the main entry point for the application, alongside some 
    configurations for the command-line arguments which can be passed to the software, and their respective
    handlers.
"""

import argparse


def run_validation_suites() -> None:
    """
        This here routine is responsible for identifying all the test suits which reside within the test directory
        and running them.

        Do note that this here routine specifically imports the unittest module within its scope, this being done 
        solely due to the fact that none of the other methods within the module require the unittest module.
    """
    import unittest

    suites = unittest.TestLoader().discover('test', pattern='*_test.py')
    unittest.TextTestRunner(verbosity=2).run(suites)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--test", help="run the unittest validation suite for the codebase.", action="store_true")
    args = parser.parse_args()

    if args.test:
        run_validation_suites()
    else:
        print("Welcome to Py-Chess!")


if __name__ == '__main__':
    main()
