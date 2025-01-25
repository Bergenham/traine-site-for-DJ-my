FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /main

COPY requirements.txt requirements.txt

EXPOSE 8000

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY mysite .

CMD ['gunicorn', 'myite.wsgi:application', 'runserver', '--bind', '0.0.0.0:8000']