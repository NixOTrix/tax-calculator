FROM node:12.2.0-alpine as build
ENV PATH /app/node_modules/.bin:$PATH
WORKDIR /app
COPY . /app
RUN npm install
RUN npm run build
