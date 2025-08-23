FROM node:20-alpine
WORKDIR /app
COPY frontend/ ./frontend
RUN cd frontend && npm install
EXPOSE 5173
CMD ["sh", "-c", "cd frontend && npm run dev -- --host 0.0.0.0"]
