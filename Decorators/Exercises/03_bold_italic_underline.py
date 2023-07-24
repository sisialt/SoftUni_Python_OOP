def make_bold(func):
    def wrapper(*args):
        result = func(*args)

        return f"<b>{result}</b>"  # "\033[1m{result}\033[0m"

    return wrapper


def make_italic(func):
    def wrapper(*args):
        result = func(*args)

        return f"<i>{result}</i>"  # "\x1B[3m{result}\x1B[0m"

    return wrapper


def make_underline(func):
    def wrapper(*args):
        result = func(*args)

        return f"<u>{result}</u>"  # "\033[4m{result}\033[0m"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
