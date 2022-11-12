# pull official base image
FROM python:3.9

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip


RUN pip install psycopg2-binary
RUN pip install numpy

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
CMD cd proyecto &&  python manage.py migrate && python manage.py runserver 0.0.0.0:8000 