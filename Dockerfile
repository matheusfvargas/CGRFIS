FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /webserv
WORKDIR /webserv
# Installing OS Dependencies

COPY requirements.txt /webserv/
RUN pip install -r requirements.txt
ADD . /webserv/
# Django service
EXPOSE 8000