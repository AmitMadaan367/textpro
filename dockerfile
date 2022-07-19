# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
# running server

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM redis:alpine
WORKDIR /code
EXPOSE 6379
CMD ["celery", "-A", "abdulla.celery", "worker" "-l" "info"]

CMD ["celery", "-A", "abdulla.celery", "beat" "-l" "info"]