import unittest
from math_quiz import random_number, choose_operator, main_calculation


class TestMathGame(unittest.TestCase):

    def random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
            

    def choose_operator(self):
        # To test if the operator is from '+' , '-', or '*' nothing else
        choose_operator = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random choices
            operator = choose_operator()
            self.assertIn(operator, choose_operator)
            pass

    def main_calculation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (6, 9, '+', '6 + 9', 15),
                (9, 3, '-', '9 - 3', 6)
            ]

            for random_first_number, random_second_number, o, expected_problem, expected_answer in test_cases:
                # To test if the randon generated problem matches with the answer
                PROBLEM, ANSWER = main_calculation(random_first_number, random_second_number, o)
                self.assertTrue(PROBLEM, ANSWER, main_calculation)

                pass

if __name__ == "__main__":
    unittest.main()
