FROM python:3.6.12-stretch
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python console database migrate
RUN python console database test
RUN python console meta sync
CMD python console run --host 0.0.0.0
# CMD uwsgi --http 127.0.0.1:3031 --wsgi-file console --callable APP --processes 4 --threads 2 --stats 127.0.0.1:9191
