from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in Musician.VALID_TYPES:
            raise ValueError("Invalid musician type!")

        musician_with_same_name = [m for m in self.musicians if m.name == name]
        if musician_with_same_name:
            raise Exception(f"{name} is already a musician!")

        create_musicians = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

        musician = create_musicians[musician_type](name, age)
        self.musicians.append(musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band_with_same_name = [b for b in self.bands if b.name == name]
        if band_with_same_name:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert_in_same_place = [c for c in self.concerts if c.place == place]
        if concert_in_same_place:
            raise Exception(f"{place} is already registered for {concert_in_same_place[0].genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician_with_same_name = [m for m in self.musicians if m.name == musician_name]
        if not musician_with_same_name:
            raise Exception(f"{musician_name} isn't a musician!")

        band_with_same_name = [b for b in self.bands if b.name == band_name]
        if not band_with_same_name:
            raise Exception(f"{band_name} isn't a band!")

        band_with_same_name[0].members.append(musician_with_same_name[0])

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band_with_same_name = [b for b in self.bands if b.name == band_name]
        if not band_with_same_name:
            raise Exception(f"{band_name} isn't a band!")

        band = band_with_same_name[0]

        musician_in_band = [m for m in band.members if m.name == musician_name]
        if not musician_in_band:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician_in_band[0])

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        if not (self.bands and self.concerts and self.musicians):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = [c for c in self.concerts if c.place == concert_place][0]
        band = [b for b in self.bands if b.name == band_name][0]

        concerts_conditions = {"Rock": {"Drummer": ["play the drums with drumsticks"],
                                        "Singer": ["sing high pitch notes"],
                                        "Guitarist": ["play rock"]},
                               "Metal": {"Drummer": ["play the drums with drumsticks"],
                                        "Singer": ["sing low pitch notes"],
                                        "Guitarist": ["play metal"]},
                               "Jazz": {"Drummer": ["play the drums with drum brushes"],
                                        "Singer": ["sing high pitch notes", "sing low pitch notes"],
                                        "Guitarist": ["play jazz"]}
                               }

        for member in band.members:
            for skill in concerts_conditions[concert.genre][member.__class__.__name__]:
                if skill not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
