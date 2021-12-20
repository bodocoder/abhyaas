From python
RUN apt update
RUN apt install -y python3-pip
RUN python3 -m pip install Django
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential
RUN pip3 install mysqlclient
WORKDIR /app
COPY . .
CMD ["python3", "manage.py","runserver","0.0.0.0:8000"]