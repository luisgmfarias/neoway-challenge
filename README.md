# Neoway Scrapping Challenge
This document gives all information needed to setup a Correios ZIP Number Range scrapper

## Setup

#### Dependencies
Main dependencies:
1. [Docker](https://www.docker.com/get-started)
2. [Python 3+](https://www.python.org/downloads/)
3. [Selenium](https://github.com/SeleniumHQ/selenium)
4. [Pandas](https://github.com/pandas-dev/pandas)
5. [PyTest](https://docs.pytest.org/en/stable/)

Run ``` pip3 install requirements.txt ``` is important to avoid any python package dependencies issues.

#### There are two ways to run this application:

**1. Running on your own environment**

Ensuring that the environment is fullfiling all required dependencies, just run:

```
python scrapping.py
```

By default (without arguments), it will scrape all data from DF (Distrito Federal), ES (Espirito Santo), GO(Goias) and MA(Maranhão)

**But It is possible to pass an argument, like:**
```
python scrapping.py SP PR PA
```

**2. Docker**

Build:

```
docker build . -t scrape-docker
```

Then, run:

```
docker run scrape-docker
```

### Testing 

Run tests:

```
pytest tests.py
```

**3** module tests were made


### Extra information

**Chrome webdriver** file is essential to run this routine, selenium driver depends on it.

If scraping ran with success, a file named **output.jsonl** is generated.
