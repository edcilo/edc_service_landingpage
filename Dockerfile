FROM python:3

# causes all output to stdout to be flushed immediately,
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

COPY . /code/

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod a+rx ./start.sh

EXPOSE 8000
CMD ["./start.sh"]
