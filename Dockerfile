FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD . /code

RUN pip install --upgrade pip
RUN pip uninstall psycopg2
RUN pip install --upgrade wheel
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

RUN ["chmod", "+x", "wait_for_postgres.sh"]
RUN ["chmod", "+x", "start.sh"]

# Server, just for Docker image, not for compose
# EXPOSE 8000
# STOPSIGNAL SIGINT
# ENTRYPOINT ["python", "manage.py"]
# CMD ["runserver", "0.0.0.0:8000"]