from dataclasses import dataclass
from typing import List


@dataclass
class Actor:
    name: str
    role: str


@dataclass
class Film:
    id: int
    title: str
    genre: str
    director: str
    year: int
    duration: int
    studio: str
    actors: List[Actor]


class FilmModel:
    def __init__(self):
        self._films: List[Film] = []
        self._next_id = 1

    def add_film(self, title, genre, director, year,
                 duration, studio, actors):

        if not title.strip() or not director.strip():
            return False

        film = Film(
            id=self._next_id,
            title=title,
            genre=genre,
            director=director,
            year=year,
            duration=duration,
            studio=studio,
            actors=actors
        )

        self._films.append(film)
        self._next_id += 1
        return True

    def get_all_films(self):
        return self._films.copy()

    def delete_film(self, film_id):
        for film in self._films:
            if film.id == film_id:
                self._films.remove(film)
                return True

        return False