# Colombia Movie Theater API

<p align="center"> 
  <img src="https://cdn.brandfetch.io/idgInoHKhi/w/820/h/166/theme/light/logo.png?c=1dxbfHSJFAPEGdCLU4o5B" width="20%" height="75">
  <img src="https://www.cinemark.com.co/static/favicon/android-icon-192x192.svg" width="20%" height="75">
  <img src="https://static.cinepolis.com/img/logo-icons/icon-144x144.png" width="75" height="75">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Royal_Films_logo.svg/3840px-Royal_Films_logo.svg.png" width="20%" height="75">
</p>

A Python API that aggregates movie showtimes from all major Colombian cinema chains in real time. Search for what's playing in your city across Cinemark, Cine Colombia, Cinépolis, and Royal Films without jumping between four different websites.

## Features

- **Multi-chain aggregation** — scrapes and merges showtimes from Cinemark, CineCol, Cinépolis, and Royal Films
- **City-based search** — filter results by city (e.g. Bogotá, Medellín, Cali)
- **Smart deduplication** — fuzzy matching groups similar film titles across chains (e.g. "Spider-Man" vs "Spider Man") so you see one clean result
- **Film + showtime lookup** — list all films currently showing, or drill into showtimes and locations for a specific title

## Tech Stack

- **Python 3.14**
- **FastAPI** - API framework
- **Selenium, Playwright** - browser automation for scraping dynamic pages
- **BeautifulSoup4** - HTML parsing
- **RapidFuzz** - fuzzy string matching for deduplication
- **Uvicorn** - ASGI server

## Project Structure

```
├── api.py                        # Main entry point & API logic
├── theaters_search/
│   ├── theaters/
│   │   ├── cinemark.py
│   │   ├── cine_col.py
│   │   ├── cinepolis.py
│   │   └── royal_films.py
│   └── dict_theaters.py          # City → theater chain mapping
└── remove_duplicates/
    └── remove_duplicates.py      # Fuzzy deduplication logic
```

## Getting Started

### Prerequisites

- Python 3.10+
- firefox (for Selenium)

### Installation

```bash
git clone https://github.com/fe15de/colombian_theaters_api.git
cd colombian_theaters_api

python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

pip install -r requirements.txt
```

### Usage

```python
from api import all_films, search_film

# Get all films showing in Bogotá
films = all_films('Bogotá')
print(films)

# Search showtimes for a specific film
results = search_film('Michael', films, 'Bogotá')
print(results)
```

## Supported Cities

Availability depends on which chains operate in each city. The `dict_theaters.py` file maps each city to its supported chains.

## How It Works

1. `all_films(city)` loops through every theater chain that operates in the given city, calls each chain's scraper, and merges the results into a single dictionary.
2. `group_similar_films()` runs fuzzy matching across all film titles to collapse near-duplicate entries into one.
3. `search_film(film_name, film, city)` queries each chain for showtimes at specific locations and returns formatted messages.

## Contributing

Pull requests are welcome. To add a new theater chain, create a new class under `theaters_search/theaters/` following the same interface as the existing scrapers, then register it in `dict_theaters.py` and `api.py`.
