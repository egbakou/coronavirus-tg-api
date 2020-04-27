<h1 align="center">
    Coronavirus Tg API
</h1>

Provides up-to-date data about Coronavirus outbreak in Togo. Includes numbers about confirmed cases, deaths and recovered.
Support unique government source.

![Travis build](https://api.travis-ci.org/egbakou/coronavirus-tg-api.svg?branch=master)[![License](https://img.shields.io/github/license/egbakou/coronavirus-tg-api)](LICENSE.md)
[![GitHub stars](https://img.shields.io/github/stars/egbakou/coronavirus-tg-api)](https://github.com/egbakou/coronavirus-tg-api/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/egbakou/coronavirus-tg-api)](https://github.com/egbakou/coronavirus-tg-api/network/members)
[![GitHub last commit](https://img.shields.io/github/last-commit/egbakou/coronavirus-tg-api)](https://github.com/egbakou/coronavirus-tg-api/commits/master)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/egbakou/coronavirus-tg-api)](https://github.com/egbakou/coronavirus-tg-api/pulls)
[![GitHub issues](https://img.shields.io/github/issues/egbakou/coronavirus-tg-api)](https://github.com/egbakou/coronavirus-tg-api/issues)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tweet](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fegbakou%2Fcoronavirus-tg-api)](https://twitter.com/intent/tweet?text=COVID19%20Tracking%20API%20For%20Togo%20&url=https%3A%2F%2Fgithub.com%2Fegbakou%2Fcoronavirus-tg-api)

## Available data-sources:

Currently 1 data-source is available to retrieve the data:

* **Togolese Government dedicated website for the covid19** - https://covid19.gouv.tg

## API Reference

All endpoints are located at ``coronavirus-tg-api.herokuapp.com/v1/`` and are accessible via https. 

You can open the URL in your browser to further inspect the response. Or you can make this curl call in your terminal to see the prettified response:

```
curl https://coronavirus-tracker-api.herokuapp.com/v1/cases | json_pp
```

### Swagger/OpenAPI

Consume our API through [our super awesome and interactive SwaggerUI](https://coronavirus-tg-api.herokuapp.com/) (on mobile, use the [mobile friendly ReDocs](https://coronavirus-tg-api.herokuapp.com/docs) instead for the best experience).

The [OpenAPI](https://swagger.io/docs/specification/about/) json definition can be downloaded at https://coronavirus-tg-api.herokuapp.com/openapi.json

### Technologies used for the project

- Python3.8 / FastApi / Unicorn / => Language & Framework
- Docker & Docker Compose => Dockerization
- Heroku => Hosting
- Travis => Build,Test, deploy, … (Github Actions soon)
- Telegram API => Bot to receive Travis job result instead of email notification

## API Endpoints

### Cases Endpoint

Getting total of confirmed cases, deaths, recovered and the last
updated date.

```http
GET /v1/cases
```

__Sample response__
```json
{
  "confirmed": 99,
  "recovered": 62,
  "deaths": 6,
  "last_updated": "2020-04-27 11:12:00"
}
```

### Sources Endpoint

Getting the data-sources that are currently available to Coronavirus Tg API to retrieve the data of the pandemic. Currently,the government website and the tracker api project.

```http
GET /v1/sources
```

__Sample response__
```json
{
  "government_website": "https://covid19.gouv.tg",
  "tracker_api_project": "https://github.com/egbakou/coronavirus-tg-api"
}
```

### Confirmed cases Endpoint

Getting confirmed cases data.

```http
GET /v1/cases/confirmed
```

__Sample response__

```json
{
  "confirmed": 99,
  "last_updated": "2020-04-27 11:12:00"
}
```

### Recovered cases Endpoint

Getting recovered cases data.

```http
GET /v1/cases/recovered
```

__Sample response__

```json
{
  "recovered": 62,
  "last_updated": "2020-04-27 11:12:00"
}
```

### Deaths data Endpoint

Getting number of deaths.

```http
GET /v1/cases/deaths
```

__Sample response__

```json
{
  "deaths": 6,
  "last_updated": "2020-04-27 11:12:00"
}
```

### __Response definitions__

| __Response Item__ | __Description__                                              | __Type__ |
| ----------------- | ------------------------------------------------------------ | -------- |
| {cases}           | total of confirmed cases, deaths, recovered and the last updated date. | Object   |
| {cases}/confirmed | The up-to-date total number of confirmed cases               | Integer  |
| {cases}/deaths    | The up-to-date total number of deaths                        | Integer  |
| {cases}/recovered | The up-to-date total number of recovered                     | Integer  |
| {sources}         | Data-sources used to provide data                            | Object   |

> We strongly recommend using the endpoint /v1/cases instead of using the endpoints returning each case.

## Wrappers

No wrapper at the moment.

## Prerequisites

You will need the following things properly installed on your computer.

* [Python 3](https://www.python.org/downloads/) (with pip)
* [pipenv](https://pypi.org/project/pipenv/)

## Installation

* `git clone https://github.com/egbakou/coronavirus-tg-api.git`
* `cd coronavirus-tg-api`

1. Make sure you have [`python3.8` installed and on your `PATH`](https://docs.python-guide.org/starting/installation/).
2. [Install the `pipenv` dependency manager](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)
   *  with [pipx](https://pipxproject.github.io/pipx/) `$ pipx install pipenv`
   * with [Homebrew/Linuxbrew](https://pipenv.readthedocs.io/en/latest/install/#homebrew-installation-of-pipenv) `$ brew install pipenv`
   * with [pip/pip3 directly](https://pipenv.readthedocs.io/en/latest/install/#pragmatic-installation-of-pipenv) `$ pip install --user pipenv`
3. Create virtual environment and install all dependencies `$ pipenv sync --dev`
4. Activate/enter the virtual environment `$ pipenv shell`

And don't despair if don't get the python setup working on the first try. No one did. Guido got pretty close... once. But that's another story. Good luck.

## Running / Development

For a live reloading on code changes.

* `pipenv run dev`

Without live reloading.

* `pipenv run start`

Visit your app at [http://localhost:8000](http://localhost:8000).

Alternatively run our API with Docker.

### Running Tests
> [pytest](https://docs.pytest.org/en/latest/)

```bash
pipenv run test
```


### Linting
> [pylint](https://www.pylint.org/)

```bash
pipenv run lint
```

### Formatting
> [black](https://black.readthedocs.io/en/stable/)

```bash
pipenv run fmt
```

### Update requirements files

```bash
invoke generate-reqs
```

[Pipfile.lock](./Pipfile.lock) will be automatically updated during `pipenv install`.

### Docker

[Our Docker](https://hub.docker.com/r/egbakou/coronavirus-tg-api/) image is based on [tiangolo/uvicorn-gunicorn-fastapi/](https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/).

```bash
invoke docker --build
```

Run with `docker run` or `docker-compose`

#### Alternate Docker images

If a full `gunicorn` deployment is unnecessary or [impractical on your hardware](https://fastapi.tiangolo.com/deployment/#raspberry-pi-and-other-architectures) consider using our single instance [`Uvicorn`](https://www.uvicorn.org/) based [Dockerfile](uvicorn.Dockerfile).


### Invoke

Additional developer commands can be run by calling them with the [python `invoke` task runner](http://www.pyinvoke.org/).
```bash
invoke --list
```

### Deploying



## Created by: Kodjo Laurent Egbakou

- LinkedIn: [Kodjo Laurent Egbakou](https://www.linkedin.com/in/laurentegbakou/)
- Twitter: [@lioncoding](https://twitter.com/lioncoding)

## Contribution

Feel free to create issues and PRs :)