FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /code/

# Server, just for Docker image, not for compose
# EXPOSE 8000
# STOPSIGNAL SIGINT
# ENTRYPOINT ["python", "manage.py"]
# CMD ["runserver", "0.0.0.0:8000"]