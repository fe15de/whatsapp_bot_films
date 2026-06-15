from theaters_search.libraries import *
from theaters_search.dict_theaters import cine_colombia_ids
    
class CineCol(Theater):
    def __init__(self):
        super().__init__('cine_col')

    def get_films(self, city):
        url = 'https://digital-api.cinecolombia.com/ocapi/v1/film-screening-dates?'
        url = self.add_ids_to_url(city,url)
        token = self.get_token()
        resp = requests.get(url,headers={"Authorization": token})
        data = resp.json()
        # data = data['data']

        return data 

    def search_showtimes_film(self, film_name, film, city):
        url_names = film.url_name
        url_name = self.verify(url_names,city)

        if not url_name:
            return f'No hay funciones de {film_name} en {self.name}'
        #----------------------------------------------------------------------------------------
        #                   Use the api instead of scraping (faster)
        #----------------------------------------------------------------------------------------
        today_date = date.today().strftime("%Y-%m-%d")
        url = f'https://funciones.cinecolombia.com/cineco/get-performances-by-params?name={url_name}&date={today_date}&city={city[:3]}'
        resp = requests.get(url)
        data = resp.json()
        if film_name not in self.locations[city]:
                self.locations[city][film_name] =  {}
        for location in data:
            mall =  location['Name']
            self.locations[city][film_name][mall] = []
            showtimes = location['showtimes']
            for type_format in showtimes:
                showtimes = type_format['performances']
                for showtime in showtimes:
                    time = datetime.fromisoformat(showtime['DateTime'])
                    self.locations[city][film_name][mall].append(time.strftime("%H:%M"))
    
    def add_ids_to_url(self,city,url):
        ids = cine_colombia_ids[city]
        i = 0
        while i < len(ids) - 1:
            url += f'siteIds={ids[i]}&'
            i += 1
        url += f'siteIds={ids[i]}'
        return url

    def get_token(self):
        captured = {}
        all_requests = []

        with sync_playwright() as p:
            browser = p.firefox.launch(headless=True)
            page = browser.new_page()

            def handle_request(request):
                all_requests.append(request.url)
                auth = request.headers.get("authorization")
                if auth:
                    if "digital-api" in request.url:
                        captured["token"] = auth

            page.on("request", handle_request)

            page.goto("https://www.cinecolombia.com/", wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(10000)

            browser.close()

        return captured.get("token")

