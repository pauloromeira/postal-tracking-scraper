# Postal Tracking Scraper
A scraper that gathers tracking events from postal services.

### Currently Suported Carriers

|Country|Carrier|
|-|-|
|Brazil|[Correios](http://www.correios.com.br/)|

## Installation
|Requirements|
|-|
|[Python 3.6](https://www.python.org/)|

### 1. Clone this repository
Clone this repository using [git](https://git-scm.com/) and cd into the project folder:
```sh
git clone https://github.com/pauloromeira/postaltracking-scraper.git && \
cd postaltracking-scraper
```

### 2. Install Python requirements
Inside project folder, install python requirements using pip:
```sh
pip install -r requirements.txt
```

## Usage
Curently, only [Correios](http://www.correios.com.br/) is suported:
```sh
scrapy crawl correios -a trackings="<tracking-number>[;<tracking-number>]*" \
-o trackings.csv -t csv
```
