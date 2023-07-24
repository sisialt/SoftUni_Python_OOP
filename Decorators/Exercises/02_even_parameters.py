def even_parameters(func):
    def wrapper(*args):
        nums = []

        for arg in args:
            if isinstance(arg, str):
                return "Please use only even numbers!"

            nums.append(arg)

        even_nums = [n for n in nums if n % 2 == 0]
        if len(nums) == len(even_nums):
            return func(*args)

        return "Please use only even numbers!"

        # for arg in args:
        #     if isinstance(arg, int):
        #         if arg % 2 == 0:
        #             continue
        #
        #     return "Please use only even numbers!"
        #
        # return func(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))

@even_parameters
def multiply(*nums):
    result = 1

    for num in nums:
        result *= num

    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

import unittest


class EvenParametersTests(unittest.TestCase):
    def test_even(self):
        @even_parameters
        def func(*args):
            return sum(args)

        result = func(4, 4, 4)
        self.assertEqual(result, 12)

    def test_odd(self):
        @even_parameters
        def func(*args):
            return sum(args)

        result = func(4, 5, 4)
        self.assertEqual(result, "Please use only even numbers!")

    def test_with_non_integer_params(self):
        @even_parameters
        def func(*args):
            return sum(args)

        result = func(4, "4", 4)
        self.assertEqual(result, "Please use only even numbers!")

    def test_with_no_params(self):
        @even_parameters
        def func():
            return "hi"

        result = func()
        self.assertEqual(result, "hi")


if __name__ == '__main__':
    unittest.main()

