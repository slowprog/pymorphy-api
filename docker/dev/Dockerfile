FROM yiivgeny/pymorphy2:0.8

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile ./
COPY Pipfile.lock ./

RUN set -ex && pipenv install --deploy --system

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]