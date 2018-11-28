# Pymorphy API

Declination in the cases of Russian phrases.

The service uses the [pymorphy2](https://pymorphy2.readthedocs.io/en/latest/) library, which uses [OpenCorpora](http://opencorpora.org/) dictionaries.

The service is based on the [yiivgeny/pymorphy2](https://hub.docker.com/r/yiivgeny/pymorphy2/) (build the latest available dictionaries) and [summerisgone/pyphrasy](https://github.com/summerisgone/pyphrasy). The service use [Django and Docker](https://gist.github.com/genomics-geek/98929a9e7ba9602fed7bfa4a5a1c5c4e).

## Usage

For development:

```shell
$ docker-compose up -d
```

For production:

```shell
$ docker-compose -f ./docker-compose.prod.yml up -d
# or
$ docker run -d --name pymorphy_api -p 8000:8000 -e ALLOWED_HOSTS=localhost slowprog/pymorphy-api
```

The service is waiting for a request with two parameters:

1. *phrase* – what to decline.
2. *forms* – one element or list of [cases and / or noun-number from pymorphy2](https://pymorphy2.readthedocs.io/en/latest/user/grammemes.html#russian-cases), separated by commas.

Example: http://localhost:8000/api/inflect?phrase=неожиданный%20дедлайн&forms=gent,plur&forms=loct

The response is in json format, which will contain an option for each of the forms:

```json
{
    "success": true,
    "data": {
        "gent,plur": "неожиданных дедлайнов",
        "loct": "неожиданном дедлайне"
    }
}
```

In case of an error, the key date will contain the text of the error:

```json
{
    "success": false,
    "data": "The phrase parameter is not specified."
}
```