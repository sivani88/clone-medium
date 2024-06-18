FROM node:20.11-alpine3.18 as base

WORKDIR /app

COPY package.json package-lock.json* ./

RUN npm install

COPY . .

CMD ["npm", "start"]
