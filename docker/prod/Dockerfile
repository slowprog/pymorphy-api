FROM yiivgeny/pymorphy2:0.8

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile ./
COPY Pipfile.lock ./

RUN set -ex && pipenv install --deploy --system

COPY . .

EXPOSE 8000

CMD [ "gunicorn", "pyphrasy.wsgi", "-b0.0.0.0:8000", "-w 4"]