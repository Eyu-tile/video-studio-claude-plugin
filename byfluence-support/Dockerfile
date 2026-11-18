FROM node:22-slim AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build && npm prune --omit=dev

FROM node:22-slim
WORKDIR /app
ENV NODE_ENV=production PORT=4000 DATA_DIR=/app/data
COPY --from=build /app /app
RUN chmod +x docker-entrypoint.sh && mkdir -p /app/data && chown -R node:node /app/data
USER node
EXPOSE 4000
VOLUME ["/app/data"]
ENTRYPOINT ["./docker-entrypoint.sh"]
