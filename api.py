from theaters_search.theaters.cinemark import Cinemark
from theaters_search.theaters.cine_col import CineCol
from theaters_search.theaters.cinepolis import Cinepolis
from remove_duplicates.remove_duplicates import group_similar_films

def all_films(city):
    pass

def search_film(films_map,film,city):
    pass



cine_col = CineCol()
cine_col.get_films('bogota')

cinemark = Cinemark()
cinemark.get_films('bogota')

cinepolis = Cinepolis()
cinepolis.get_films('bogota')
 
films = {**cine_col.films['bogota'],**cinemark.films['bogota'],**cinepolis.films['bogota']}
films = group_similar_films(films)
#print(films)
cinepolis.search_showtimes_film(films,'Demon Slayer: Kimetsu no Yaiba - Castillo Infinito','bogota')
cinemark.search_showtimes_film(films,'Demon Slayer: Kimetsu no Yaiba - Castillo infinito','bogota')
print(cinemark.locations['bogota']['Demon Slayer: Kimetsu no Yaiba - Castillo infinito'])
cine_col.search_showtimes_film(films,'Demon Slayer: Kimetsu no Yaiba - Castillo infinito','bogota')