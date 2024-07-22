FROM node:20-alpine

WORKDIR /app

RUN apk update && apk upgrade

COPY ./app/package*.json /app/

RUN yarn install
RUN yarn build

