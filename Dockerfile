FROM rasa/rasa:1.10.3

WORKDIR /app
COPY /app
COPY . /app
COPY ./data /app/data
COPY /ssl /app/ssl

RUN rasa train

VOLUME /app
VOLUME /app/data
VOLUME /app/models
VOLUME /app/ssl

CMD ["run","-m","/app/models","--enable-api","--cors","*","--debug"]
