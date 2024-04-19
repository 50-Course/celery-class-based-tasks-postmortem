FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN python install -U requirements.txt

EXPOSE 8000

