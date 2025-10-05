from theaters_search.libraries import *

class Cinepolis(Theater):
    def __init__(self):
        super().__init__('cinepolis')

    def get_films(self, city):
        url = theaters_url[self.name][0].format(city=city)
        soup = self.get_driver(url,'listaCarteleraHorario')

        if city not in self.films:
            self.films[city] = {}
            self.locations[city] = {}
        #-------------------------------------------------------------------
        #               Getting the name of the malls
        #-------------------------------------------------------------------
        for complejo in soup.find_all("div", class_="divComplejo"):
            mall = complejo.find("h2").get_text(strip=True).replace(" ?", "")
            #-------------------------------------------------------------------
            #               Getting the name of the films and showtimes
            #-------------------------------------------------------------------
            for film in complejo.find_all("article", class_="tituloPelicula"):
                name =film.find("a", class_="datalayer-movie").get_text(strip=True)
                name= self.normalize_name(name)
                url_name = self.url_name(name)
                self.films[city][name] = url_name

                section = film.find('div',class_='descripcion')
                showtimes = [
                    t.get_text(strip=True)
                    for t in section.find_all("a", class_="ng-binding")
                ]
                if name not in self.locations[city]:
                    self.locations[city][name] =  {}
                
                self.locations[city][name][mall] = showtimes[1:]

        

    def search_showtimes_film(self, films, film, city):
        if film in self.films[city]:
            return self.locations[city][film]
        else:
            return f'No hay funciones de {film} en {self.name}'