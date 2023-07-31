FROM python:3.8 as final

EXPOSE 8000
WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY . /code
