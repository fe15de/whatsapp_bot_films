from theaters_search.theaters.cinemark import Cinemark
from theaters_search.theaters.cine_col import CineCol
from theaters_search.theaters.cinepolis import Cinepolis
from theaters_search.theaters.royal_films import RoyalFilms
from remove_duplicates.remove_duplicates import group_similar_films
from theaters_search.dict_theaters import theaters_by_city

royal_films = RoyalFilms()
cinepolis = Cinepolis()
cine_col = CineCol()
cinemark = Cinemark()

theaters_names = {
        "cine_col": cine_col,
        "cinemark": cinemark,
        "cinepolis": cinepolis,
        "royal_films": royal_films,
    }

def all_films(city):
    films = {}

    for theater in theaters_by_city:
        if city in theaters_by_city[theater]:
            theaters_names[theater].get_films(city)
            films.update(theaters_names[theater].films[city])

    films = group_similar_films(films)
    return films

def search_film(film_name,film,city):
    msg = ''
    for theater in theaters_by_city:
        if city in theaters_by_city[theater]:
            theaters_names[theater].search_showtimes_film(film_name, film, city)
            msg += theaters_names[theater].message_locations(city,film_name)
    return msg
#------------------------------------------------------------------------
#                       TESTING IF THE API IS WORKING
#------------------------------------------------------------------------
""" films = all_films('Bogotá')
print(films.keys())
search_film(films,'Demon Slayer: Kimetsu no Yaiba - Castillo infinito','Bogotá') """

    