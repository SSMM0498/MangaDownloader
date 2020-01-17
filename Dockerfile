# FROM ubuntu
FROM python:alpine3.7
COPY . /mangadownloader
WORKDIR /mangadownloader
RUN export PATH=$PATH":$HOME/bin"
# RUN pip install -r ./requirements.txt
EXPOSE 5000
VOLUME [ "/mangadownloader" ]