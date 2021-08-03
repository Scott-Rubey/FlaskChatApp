FROM python:alpine
MAINTAINER Scott Rubey "scott.d.rubey@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD exec gunicorn --bind :${PORT:-80} --workers 1 --threads 8 application:application