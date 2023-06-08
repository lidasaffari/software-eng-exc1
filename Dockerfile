FROM python:3.8

WORKDIR /code

COPY req.txt /code/

RUN pip install -U pip
RUN pip install -r requirments.txt

COPY . /code/

EXPOSE 8000

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
