FROM node

WORKDIR /src
COPY package.json package-lock.json /src/
EXPOSE 3001 3002 3003

COPY .. .
CMD ["npm", "run", "start"]