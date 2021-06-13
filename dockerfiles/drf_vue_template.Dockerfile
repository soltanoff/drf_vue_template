FROM python:3.6.9
MAINTAINER Ilya Soltanov <piccadillable@gmail.com>
ENV PYTHONBUFFERED 1
COPY ./requirements.txt /drf_vue_template/requirements.txt
WORKDIR /drf_vue_template
RUN pip install -r requirements.txt
COPY . /drf_vue_template
