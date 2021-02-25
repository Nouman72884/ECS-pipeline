FROM python:3.4-alpine

WORKDIR /work

ADD  . /work

RUN pip install -r requirements.txt

EXPOSE 5000
 
CMD ["python","app.py"]
