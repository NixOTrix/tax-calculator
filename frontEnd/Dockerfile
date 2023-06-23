FROM node:18 as build
ENV PATH /app/node_modules/.bin:$PATH

RUN mkdir /app
WORKDIR /app
COPY ./tax-calculator ./
RUN npm install
RUN npm install -g serve
RUN npm run build
CMD cd build && serve

