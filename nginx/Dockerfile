FROM node:23-alpine AS build-stage

WORKDIR /frontend

COPY frontend/package*.json ./

RUN npm install

COPY frontend/ .

RUN npm run build

# Production stage
FROM nginx:alpine AS production-stage

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=build-stage /frontend/dist /usr/share/nginx/html

COPY --from=build-stage /frontend/src/images /usr/share/nginx/html/src/images

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]