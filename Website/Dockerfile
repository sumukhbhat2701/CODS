FROM ubuntu:18.04

RUN apt-get update && apt-get -y install curl gnupg && curl -sL https://deb.nodesource.com/setup_13.x  | bash - && apt-get -y install nodejs


WORKDIR /app/Website
COPY . /app/Website

RUN npm install 

VOLUME /app/Website

CMD npm start
