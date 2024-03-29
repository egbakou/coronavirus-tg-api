#FROM python:3.8-slim
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ENV VARIABLE_NAME APP

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r  /app/requirements.txt

COPY . /app/

EXPOSE 80

CMD ["uvicorn", "app.main:APP", "--host", "0.0.0.0", "--port", "80"]