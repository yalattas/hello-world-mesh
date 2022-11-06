FROM python:3.9.7-slim
RUN pip install --upgrade pip
WORKDIR /app

RUN apt-get update && apt-get install -y vim
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000:8000

ENTRYPOINT [ "python", "main.py" ]