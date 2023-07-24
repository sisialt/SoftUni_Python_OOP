import os


class store_results:
    def __init__(self, func):
        self.func = func
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(self.root_dir, "results.txt")

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a") as file:
            return file.write(f"Function {self.func.__name__} was called. Result: {self.func(*args, **kwargs)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)