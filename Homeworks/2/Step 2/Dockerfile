FROM python:3.11.0a6-alpine3.15

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python app.py