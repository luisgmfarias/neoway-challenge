FROM python:3
LABEL version=1.0

RUN apt-get update -y 
RUN apt-get install -y python3-pip build-essential

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "scrapping.py"]
