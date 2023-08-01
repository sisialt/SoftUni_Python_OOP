from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        existing_user = [u for u in self.users_collection if u.username == username]
        if existing_user:
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

        # it never raises exception because it was creating new objects, that are not in the list

        # obj = User(username, age)
        #
        # if obj not in self.users_collection:
        #     self.users_collection.append(obj)
        #     return f"{username} registered successfully."
        #
        # raise Exception("User already exists!")

    @staticmethod
    def is_username_owner(username: str, movie: Movie):
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

    def is_movie_in_movies_collection(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

    def find_existing_user(self, username):
        user = [u for u in self.users_collection if u.username == username]
        if user:
            return user[0]
        return None

    def upload_movie(self, username: str, movie: Movie):
        user = self.find_existing_user(username)
        if not user:
            raise Exception("This user does not exist!")

        self.is_username_owner(username, movie)

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        self.is_movie_in_movies_collection(username, movie)
        self.is_username_owner(username, movie)
# check
        for kwarg in kwargs:
            setattr(movie, kwarg, kwargs[kwarg])

            # if kwarg == 'title':
            #     movie.title = kwargs[kwarg]
            # elif kwarg == 'likes':
            #     movie.likes = kwargs[kwarg]
            # elif kwarg == 'age_restriction':
            #     movie.age_restriction = kwargs[kwarg]
            # elif kwarg == 'owner':
            #     movie.owner = kwargs[kwarg]
            # elif kwarg == 'year':
            #     movie.year = kwargs[kwarg]

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        self.is_movie_in_movies_collection(username, movie)
        self.is_username_owner(username, movie)

        self.movies_collection.remove(movie)

        user = self.find_existing_user(username)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        if movie.owner.username == username:  # not if movie.owner == username
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        user = self.find_existing_user(username)

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.find_existing_user(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        result = []
        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        if not sorted_movies:
            return "No movies found."

        for movie in sorted_movies:
            result.append(movie.details())

        return '\n'.join(result)

    def __str__(self):
        if self.users_collection:
            result = ', '.join(s.username for s in self.users_collection)
        else:
            result = "No users."

        if self.movies_collection:
            result2 = ', '.join(m.title for m in self.movies_collection)
        else:
            result2 = "No movies."

        return f"All users: "\
                f"{result}\n"\
                f"All movies: "\
                f"{result2}"