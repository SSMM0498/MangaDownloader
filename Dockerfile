FROM python:alpine3.7
FROM ubuntu
COPY . /mangadownloader
WORKDIR /mangadownloader
# RUN pip install -r ./requirements.txt
EXPOSE 5000
CMD ./dm.sh