FROM tiangolo/uwsgi-nginx-flask

COPY ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

ENV CACHE_EXPIRATION_TIME 300
ENV CACHE_PORT 80
ENV COIN_NAME 'bitcoin'

COPY app.py /app/main.py
