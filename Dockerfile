From python:3.9


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /backend_rez
WORKDIR /backend_rez
COPY requirements.txt /backend_rez/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /backend_rez/
RUN python manage.py makemigrations
