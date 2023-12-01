FROM --platform=$BUILDPLATFORM python:3.12.0 AS builder
EXPOSE 8000
WORKDIR /app
COPY requirement.txt /app
RUN pip install -r requirement.txt --no-cache-dir
COPY . /app
CMD ["bash" , "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
