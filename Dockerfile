FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt  /app/requirements.txt

ADD entrypoint.sh /app/entrypoint.sh

RUN chmod a+x /app/entrypoint.sh

RUN pip install -r requirements.txt



COPY . /app


ENTRYPOINT ["/app/entrypoint.sh"]