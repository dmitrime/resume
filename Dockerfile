FROM ubuntu:latest
MAINTAINER Dmitri Melnikov
EXPOSE 80

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /resume
WORKDIR /resume
RUN pip install -r requirements.txt

CMD ["./gunicorn.sh"]
