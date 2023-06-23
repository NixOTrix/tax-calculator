FROM node:12.2.0-alpine as build
ENV PATH /app/node_modules/.bin:$PATH
WORKDIR /app
COPY ./start.sh . 
# copy the build folder to here

RUN npm install -g serve
ENTRYPOINT [ "start.sh" ]
# RUN npm install
# RUN npm run build



