FROM python:alpine3.7
ADD download_manga /
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ./dm.sh