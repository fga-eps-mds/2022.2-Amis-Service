FROM python:3.10.4-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
 
EXPOSE 8080

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0","--port", "8080","--reload"]