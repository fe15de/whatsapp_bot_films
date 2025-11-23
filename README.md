# whatsapp_bot_films

A WhatsApp bot (Python) for checking movie listings in Colombia. It scrapes data from Cine Colombia, Cinepolis, Cinemark, Royal Films, and others, then serves everything through a FastAPI backend so users can query showtimes directly from WhatsApp.

## 📘 Table of Contents

- [Description](#description)
- [Features](#features)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints / Commands](#endpoints--commands)
- [Security](#security)
- [Contribution](#contribution)
- [License](#license)

## Description

This project provides a WhatsApp bot that delivers movie listings and showtimes from multiple cinema chains in Colombia. It scrapes data from each chain's website and exposes unified movie information through a FastAPI backend.

The goal is simple: make movie discovery less painful than browsing each cinema site individually.

## Features

- Web scraping for movie listings across several cinema chains
- Internal API implemented with FastAPI
- WhatsApp integration for receiving queries and sending responses
- Theater search functionality
- Duplicate-cleaning utilities
- Basic security logic

## Architecture

Repository structure:

- `theaters_search` — search theaters by city or name
- `remove_duplicates` — utilities for deduplication
- `model` — data models for theaters, movies, and showtimes
- `security` — basic validations and access rules
- `whatsapp` — webhook handling and WhatsApp logic
- `api.py` — API endpoints
- `main.py` — application entrypoint

## Requirements

- Python 3.x
- Dependencies from `requirements.txt`
- Internet connection for scraping
- WhatsApp webhook credentials and configuration

## Installation

```sh
git clone https://github.com/fe15de/whatsapp_bot_films.git
cd whatsapp_bot_films
```

Create a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
```

Install dependencies:

```sh
pip install -r requirements.txt
```

## Architecture

/theaters_search # Search theaters by city or name
/remove_duplicates # Deduplication utilities
/model # Movie, showtime, and theater data models
/security # Validation and basic security rules
/whatsapp # WhatsApp webhook and message handling
api.py # API endpoints
main.py # Application entrypoint

Configure your WhatsApp webhook to point to your server URL.

Use WhatsApp commands to retrieve movies, theaters, and showtimes.

## Endpoints / Commands

### API Endpoints

- `/movies` — returns movie listings
- `/theaters` — returns available theaters
- `/showtimes?theater_id={id}` — returns showtimes for a specific theater

### WhatsApp Commands

- `!movies`
- `!theaters`
- `!showtimes <theater>`

## Security

- Input validation for safe scraping
- Token validation for restricted API access
- Throttling or caching to avoid stressing cinema websites
- Error handling for layout changes in external websites

## Contribution

1. Fork this repository
2. Create a new branch (feature or bugfix)
3. Make your changes
4. Submit a Pull Request with a clear description
