FROM python:3.11.5-alpine

WORKDIR /app

COPY  requirements.txt .

RUN python -m pip install -r requirements.txt

ENV FLASK_APP=__init__.py
ENV PYTHONPATH="/app:$PYTHONPATH"


COPY . /app

CMD flask run --host 0.0.0.0 -p 8080
