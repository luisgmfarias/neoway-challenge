FROM python:3
MAINTAINER Luis Farias <luisgmfarias@gmail.com>

RUN apt-get update -y 
RUN apt-get install -y python3-pip build-essential

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "scrapping.py"]
