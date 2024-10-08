FROM node

WORKDIR /src
COPY package.json package-lock.json /src/
EXPOSE 3000

COPY ../.. .
RUN ["npm", "install"]

CMD ["npm", "run", "start"]