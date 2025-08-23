FROM node:20-alpine
WORKDIR /app
COPY ./frontend/ ./frontend
RUN npm install --prefix ./frontend
EXPOSE 5173
CMD ["sh", "-c", "npm run dev --prefix ./frontend -- --host 0.0.0.0"]
