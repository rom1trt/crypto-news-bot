FROM python:3.8-buster

WORKDIR /project

# main.py file
COPY main.py .

# app folder
COPY app ./app

# Packages
RUN pip install pandas
RUN pip install tweepy
RUN pip install googletrans==4.0.0-rc1

CMD ["python3", "./main.py"]
