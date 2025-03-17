FROM node:23-alpine as build-stage

WORKDIR /app/frontend

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]