FROM node:10.15.2-alpine
RUN mkdir /frontend
WORKDIR /frontend
COPY package.json /frontend/package.json
COPY . /frontend
RUN npm install
ENTRYPOINT ["npm"]
CMD ["start"]
