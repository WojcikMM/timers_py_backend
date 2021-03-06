FROM python:3.7
RUN mkdir timers-backend-app
WORKDIR /timers-backend-app
COPY requirements.txt /timers-backend-app/
RUN pip3 install --no-cache-dir -r requirements.txt && rm requirements.txt
COPY ./src/ /timers-backend-app
EXPOSE 8080
CMD ["python","./app.py"]
