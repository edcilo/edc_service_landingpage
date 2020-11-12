FROM python:3

ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt
RUN chmod a+rx ./start.sh

CMD ["./start.sh"]
