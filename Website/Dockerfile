#FROM ubuntu:18.04

#RUN apt-get update && apt-get install curl && curl -sL https://deb.nodesource.com/setup_18.x |#bash - && apt-get install nodejs
#&& apt-get install curl gnupg 

#WORKDIR /app/Website
#COPY . /app/Website

#RUN npm install 

#VOLUME /app/Website

#CMD npm start
FROM node:12

# Create app directory
WORKDIR /app/Website

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json /app/Website/

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . /app/Website/

VOLUME /app/Website

EXPOSE 3000
CMD [ "node", "server.js" ]
