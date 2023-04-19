from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        filtered_movies = list(
            filter(lambda x: x is not None, map(MapExercise.filter_movies, list_of_movies))
        )

        return sum(filtered_movies) / len(filtered_movies)

    @staticmethod
    def filter_movies(movie: dict) -> float:
        count_country = len(movie["country"].split(","))
        rating = movie["rating_kinopoisk"]
        return float(rating) if rating and float(rating) > 0 and count_country > 1 else None

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        return sum(map(lambda x: MapExercise.count_chars_in_movie(x, "и", rating), list_of_movies))

    @staticmethod
    def count_chars_in_movie(movie: dict, char: str, rating: Union[float, int]) -> int:
        if movie["rating_kinopoisk"] and float(movie["rating_kinopoisk"]) >= rating:
            return movie["name"].count(char)
        return 0
