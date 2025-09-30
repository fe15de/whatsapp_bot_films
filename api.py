from theaters_search.theaters.cinemark import Cinemark
from theaters_search.theaters.cine_col import CineCol
from theaters_search.theaters.cinepolis import Cinepolis
from theaters_search.theaters.royal_films import RoyalFilms
from remove_duplicates.remove_duplicates import group_similar_films

def all_films(city):
    pass

def search_film(films_map,film,city):
    pass


royal_films = RoyalFilms()
royal_films.get_films('Bogotá')

cine_col = CineCol()
cine_col.get_films('bogota')

cinemark = Cinemark()
cinemark.get_films('bogota')

cinepolis = Cinepolis()
cinepolis.get_films('bogota')
 
films = {
    **cine_col.films['bogota'],
    **cinemark.films['bogota'],
    **cinepolis.films['bogota'],
    **royal_films.films['Bogotá'],
}
films = group_similar_films(films)
#print(films)

royal_films.search_showtimes_film(films,'Demon Slayer: Kimetsu no Yaiba - Castillo infinito','Bogotá')
print('ROYAL FILMS')
print(royal_films.locations['Bogotá']['Demon Slayer: Kimetsu no Yaiba - Castillo infinito'])

cinepolis.search_showtimes_film(films,'Demon Slayer: Kimetsu no Yaiba - Castillo infinito','bogota')
print('CINEPOLIS')
print(cinepolis.locations['bogota']['Demon Slayer: Kimetsu no Yaiba - Castillo Infinito'])

cinemark.search_showtimes_film(films,'Demon Slayer: Kimetsu no Yaiba - Castillo infinito','bogota')
print('CINEMARK')
print(cinemark.locations['bogota']['Demon Slayer: Kimetsu no Yaiba - Castillo infinito'])

print('CINE COLOMBIA')
cine_col.search_showtimes_film(films,'Demon Slayer: Kimetsu no Yaiba - Castillo infinito','bogota')