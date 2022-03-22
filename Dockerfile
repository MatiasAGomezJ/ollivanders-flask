FROM python:3.8-alpine

EXPOSE 5000

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

CMD ["python3", "api.py"]