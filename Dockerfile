FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . .

RUN chmod +x start.sh

EXPOSE 8000
