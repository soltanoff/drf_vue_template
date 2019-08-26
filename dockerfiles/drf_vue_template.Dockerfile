FROM python:3.6
MAINTAINER Ilya Soltanov <piccadillable@gamil.com>
ENV PYTHONBUFFERED 1
COPY ./requirements.txt /drf_vue_template/requirements.txt
WORKDIR /drf_vue_template
RUN chmod +x wait-for-it.sh
RUN pip install -r requirements.txt
COPY . /drf_vue_template