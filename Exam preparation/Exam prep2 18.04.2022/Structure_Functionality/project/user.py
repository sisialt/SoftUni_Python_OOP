from project.movie_specification.movie import Movie


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: list[Movie] = []
        self.movies_owned: list[Movie] = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Invalid username!")

        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")

        self.__age = value

    def __str__(self):
        result = []
        for movie in self.movies_liked:
            result.append(movie.details())
        if not result:
            result = "No movies liked."
        else:
            result = '\n'.join(result)
        result2 = []
        for movie in self.movies_owned:
            result2.append(movie.details())
        if not result2:
            result2 = "No movies owned."
        else:
            result2 = '\n'.join(result2)

        return (f"Username: {self.username}, Age: {self.age}\n"
                f"Liked movies:\n"
                f"{result}\n"
                f"Owned movies:\n"
                f"{result2}")
